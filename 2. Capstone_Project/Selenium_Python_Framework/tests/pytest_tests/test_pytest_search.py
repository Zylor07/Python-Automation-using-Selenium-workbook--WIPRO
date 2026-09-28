import pytest
from framework.data import SEARCH_CASES
from pages.search_page import SearchPage


@pytest.mark.parametrize("case", SEARCH_CASES, ids=lambda case: case["case_id"])
def test_product_search(driver, settings, case):
    page = SearchPage(driver, settings).open().search(case["query"])
    if case["expected_type"] == "product":
        assert case["expected_product"] in page.product_names()
    elif case["expected_type"] == "no_results":
        assert page.has_no_results()
    else:
        raise ValueError(f"Unknown expected_type: {case['expected_type']}")
