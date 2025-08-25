import pytest
import allure
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_make_report(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        if 'response' in item.funcargs:
            response = item.funcargs['response']
            allure.attach(
                f"Request URL: {response.request.url}\n"
                f"Request Method: {response.request.method}\n"
                f"Request Body: {response.request.body}\n"
                f"Response Status Code: {response.status_code}\n"
                f"Response Body: {response.text}",
                name="API Request/Response",
                attachment_type=AttachmentType.TEXT
            )
