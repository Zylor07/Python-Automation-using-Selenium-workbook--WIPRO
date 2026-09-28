import os
import pytest
from framework.data import LOGIN_CASES
from pages.login_page import LoginPage


@pytest.mark.parametrize("case", LOGIN_CASES, ids=lambda case: case["case_id"])
def test_invalid_login(driver, settings, case):
    page = LoginPage(driver, settings).open().login(case["email"], case["password"])
    assert case["expected_message"] in page.error_message()


@pytest.mark.skipif(not (os.getenv("TEST_EMAIL") and os.getenv("TEST_PASSWORD")),
                    reason="Set TEST_EMAIL and TEST_PASSWORD for the optional registered account test")
def test_valid_login(driver, settings):
    page = LoginPage(driver, settings).open().login(os.environ["TEST_EMAIL"], os.environ["TEST_PASSWORD"])
    assert page.is_account_open()
