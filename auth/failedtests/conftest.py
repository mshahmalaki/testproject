import pytest
from auth import create_app


@pytest.fixture()
def app():
    app = create_app()
    return app


@pytest.fixture()
def client(app):
    return app.test_client()
