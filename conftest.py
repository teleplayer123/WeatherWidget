import pytest

from config import config

@pytest.fixture(scope="session")
def index_url():
    host = config["network"]["host"]
    port = config["network"]["port"]
    return f"http://{host}:{port}/index"