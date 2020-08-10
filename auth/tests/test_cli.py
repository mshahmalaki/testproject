import pytest


@pytest.mark.run(order=2)
def test_app_cli_test(runner):
    result = runner.invoke(args=["app", "testdb"])
    assert "FAILED" not in result.output
