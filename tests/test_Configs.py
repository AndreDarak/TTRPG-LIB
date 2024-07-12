from ward import fixture
from fastapi.testclient import TestClient
from TTRPG.app import app


@fixture
def client():
    return TestClient(app)
