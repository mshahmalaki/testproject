import pytest


@pytest.mark.parametrize(
    ("endpoint", "json", "status_code"),
    [
        ("/invoices", {
            'user_id': 1000,
            'amount': 0
        }, 500),
    ]
)
def test_create_invoice(client, endpoint, json, status_code):
    result = client.post(endpoint, json=json)
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "status_code"),
    [
        ("/invoices/0", 500),
    ]
)
def test_delete_invoice(client, endpoint, status_code):
    result = client.delete(endpoint)
    assert result.status_code == status_code
