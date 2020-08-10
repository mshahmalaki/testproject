import pytest


pytest.global_invoice_id = None


@pytest.mark.parametrize(
    ("endpoint", "json", "status_code"),
    [
        ("/invoices/0", {}, 405),
        ("/invoices", {}, 400),
        ("/invoices", {'amount': '0'}, 400),
        ("/invoices", {
            'user_id': 1000,
            'amount': 0
        }, 201),
    ]
)
def test_create_invoice(client, endpoint, json, status_code):
    result = client.post(endpoint, json=json)
    json_data = result.get_json()
    if "invoice" in json_data:
        pytest.global_invoice_id = json_data["invoice"]["id"]
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "status_code", "real_invoice"),
    [
        ("/invoices", 200, False),
        ("/invoices/0", 404, False),
        ("/invoices/", 200, True),
    ]
)
def test_get_invoice(client, endpoint, status_code, real_invoice):
    if real_invoice:
        result = client.get(endpoint+str(pytest.global_invoice_id))
    else:
        result = client.get(endpoint)
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "json", "status_code", "real_user"),
    [
        ("/invoices", {}, 405, False),
        ("/invoices/0",{
            "user_id": 1000,
            "amount": 0
        }, 404, False),
        ("/invoices/",{
            "user_id": 1000,
            "amount": 0
        }, 204, True),
    ]
)
def test_update_invoice(client, endpoint, json, status_code, real_user):
    if real_user:
        result = client.put(endpoint+str(pytest.global_invoice_id), json=json)
    else:
        result = client.put(endpoint, json=json)
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "status_code", "real_delete"),
    [
        ("/invoices", 405, False),
        ("/invoices/0", 404, False),
        ("/invoices/", 204, True),
    ]
)
def test_delete_invoice(client, endpoint, status_code, real_delete):
    if real_delete:
        result = client.delete(endpoint+str(pytest.global_invoice_id))
    else:
        result = client.delete(endpoint)
    assert result.status_code == status_code
