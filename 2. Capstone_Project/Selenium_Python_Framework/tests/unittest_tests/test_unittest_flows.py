import os
import unittest
from framework.browser import create_driver
from framework.config import load_settings
from framework.data import LOGIN_CASES, SEARCH_CASES
from pages.login_page import LoginPage
from pages.search_page import SearchPage


class BrowserTest(unittest.TestCase):
    def setUp(self):
        self.settings = load_settings()
        self.driver = create_driver(self.settings)

    def tearDown(self):
        self.driver.quit()


class LoginTests(BrowserTest):
    def test_invalid_login_cases(self):
        for case in LOGIN_CASES:
            with self.subTest(case=case["case_id"]):
                page = LoginPage(self.driver, self.settings).open()
                page.login(case["email"], case["password"])
                self.assertIn(case["expected_message"], page.error_message())

    @unittest.skipUnless(os.getenv("TEST_EMAIL") and os.getenv("TEST_PASSWORD"),
                         "Set TEST_EMAIL and TEST_PASSWORD for the optional registered account test")
    def test_valid_login(self):
        page = LoginPage(self.driver, self.settings).open()
        page.login(os.environ["TEST_EMAIL"], os.environ["TEST_PASSWORD"])
        self.assertTrue(page.is_account_open())


class SearchTests(BrowserTest):
    def test_search_cases(self):
        for case in SEARCH_CASES:
            with self.subTest(case=case["case_id"]):
                page = SearchPage(self.driver, self.settings).open().search(case["query"])
                if case["expected_type"] == "product":
                    self.assertIn(case["expected_product"], page.product_names())
                elif case["expected_type"] == "no_results":
                    self.assertTrue(page.has_no_results(), f"Expected no products for {case['query']}")
                else:
                    self.fail(f"Unknown expected_type: {case['expected_type']}")
