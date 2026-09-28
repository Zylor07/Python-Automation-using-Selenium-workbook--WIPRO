"""Run unittest in its own suite and write a standalone HTML summary."""
import html
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
from framework.config import ROOT
from framework.evidence import save_failure


class EvidenceResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
        self._failed_tests = set()

    def _record_problem(self, test, error, status):
        image = None
        if getattr(test, "driver", None) is not None:
            try:
                image = save_failure(test.driver, test.id())
            except Exception as exc:
                print(f"Screenshot unavailable: {exc}", file=self.stream)
        self.records.append((test.id(), status, self._exc_info_to_string(error, test), image))
        self._failed_tests.add(test)

    def addFailure(self, test, err):
        self._record_problem(test, err, "FAIL")
        super().addFailure(test, err)

    def addError(self, test, err):
        self._record_problem(test, err, "ERROR")
        super().addError(test, err)

    def addSubTest(self, test, subtest, err):
        if err is not None:
            self._record_problem(test, err, "FAIL (subtest)")
        super().addSubTest(test, subtest, err)

    def addSkip(self, test, reason):
        self.records.append((test.id(), "SKIP", reason, None))
        super().addSkip(test, reason)

    def addSuccess(self, test):
        if test not in self._failed_tests:
            self.records.append((test.id(), "PASS", "", None))
        super().addSuccess(test)


def main():
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(ROOT / "tests" / "unittest_tests"), pattern="test_unittest_*.py", top_level_dir=str(ROOT)
    )
    result = unittest.TextTestRunner(verbosity=2, resultclass=EvidenceResult).run(suite)
    output = ROOT / "reports" / "unittest_report.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for name, status, message, image in result.records:
        link = f'<a href="../screenshots/{html.escape(image.name)}">Screenshot</a>' if image else ""
        rows.append(f"<tr><td>{html.escape(name)}</td><td>{html.escape(status)}</td>"
                    f"<td><details><summary>Details</summary><pre>{html.escape(message)}</pre></details></td><td>{link}</td></tr>")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    output.write_text("<!doctype html><html lang='en'><meta charset='utf-8'><title>Unittest results</title>"
                      "<style>body{font-family:Arial,sans-serif;margin:2rem}table{border-collapse:collapse;width:100%}"
                      "th,td{border:1px solid #999;padding:.5rem;text-align:left;vertical-align:top}pre{white-space:pre-wrap}</style>"
                      f"<h1>Unittest results</h1><p>{timestamp} | Tests run: {result.testsRun} | "
                      f"Failures: {len(result.failures)} | Errors: {len(result.errors)} | "
                      f"Skipped: {len(result.skipped)}</p><table><tr><th>Test</th><th>Status</th>"
                      f"<th>Traceback / reason</th><th>Evidence</th></tr>{''.join(rows)}</table></html>", encoding="utf-8")
    print(f"HTML report: {output}")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
