import pytest
from api_client import ApiClient


@pytest.fixture(scope="session")
def api(request):
    base_url = request.config.getoption("--url")
    return ApiClient(base_url)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        help="input api url",
        default="https://jsonplaceholder.typicode.com",
    ),
