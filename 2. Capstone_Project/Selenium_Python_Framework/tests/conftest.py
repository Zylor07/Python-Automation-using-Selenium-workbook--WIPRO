"""Pytest browser fixture and failure screenshot attachment."""
import base64
import pytest
import pytest_html
from framework.browser import create_driver
from framework.config import load_settings
from framework.evidence import save_failure


@pytest.fixture
def settings():
    return load_settings()


@pytest.fixture
def driver(request, settings):
    browser = create_driver(settings)
    request.node.browser = browser
    try:
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    browser = getattr(item, "browser", None)
    if report.failed and browser is not None and report.when in {"setup", "call"}:
        try:
            image_path = save_failure(browser, item.nodeid)
            extras = list(getattr(report, "extras", []))
            encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
            extras.append(pytest_html.extras.png(encoded, name="Failure screenshot"))
            report.extras = extras
            print(f"\nFailure screenshot: {image_path}")
        except Exception as error:
            print(f"\nUnable to save failure screenshot: {error}")
