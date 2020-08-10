import pytest


@pytest.mark.run(order=0)
def test_env(app):
    assert app.config["ENV"] == "development"
