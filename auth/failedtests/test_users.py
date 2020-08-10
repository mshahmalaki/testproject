import pytest


@pytest.mark.parametrize(
    ("endpoint", "json", "status_code"),
    [
        ("/users", {
            'username': 'pytest',
            'password': 'pytest',
            'address': 'pytest'
        }, 500),
    ]
)
def test_create_user(client, endpoint, json, status_code):
    result = client.post(endpoint, json=json)
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "status_code"),
    [
        ("/users/0", 500)
    ]
)
def test_delete_user(client, endpoint, status_code):
    result = client.delete(endpoint)
    assert result.status_code == status_code
