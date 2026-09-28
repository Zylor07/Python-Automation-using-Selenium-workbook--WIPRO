"""CSV fixture loader with schema checks."""
import csv
from pathlib import Path
from framework.config import ROOT


def read_cases(filename: str, required: set[str]) -> list[dict[str, str]]:
    path = ROOT / "data" / filename
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = set(reader.fieldnames or [])
        if missing := required - fields:
            raise ValueError(f"{path.name}: missing columns {sorted(missing)}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path.name}: no cases")
    if any(not row["case_id"].strip() for row in rows):
        raise ValueError(f"{path.name}: empty case_id")
    return rows


LOGIN_CASES = read_cases("login_cases.csv", {"case_id", "email", "password", "expected_message"})
SEARCH_CASES = read_cases("search_cases.csv", {"case_id", "query", "expected_product", "expected_type"})
