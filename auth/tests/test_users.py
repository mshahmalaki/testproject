import pytest


pytest.global_user_id = None


@pytest.mark.parametrize(
    ("endpoint", "json", "status_code"),
    [
        ("/users/0", {}, 405),
        ("/users", {}, 400),
        ("/users", {'username': 'pytest'}, 400),
        ("/users", {
            'username': 'pytest',
            'password': 'pytest',
            'address': 'pytest'
        }, 201),
        ("/users", {
            'username': 'pytest',
            'password': 'pytest',
            'address': 'pytest'
        }, 409),
    ]
)
def test_create_user(client, endpoint, json, status_code):
    result = client.post(endpoint, json=json)
    json_data = result.get_json()
    if "user" in json_data:
        pytest.global_user_id = json_data["user"]["id"]
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "status_code", "real_user"),
    [
        ("/users", 200, False),
        ("/users/0", 404, False),
        ("/users/", 200, True),
    ]
)
def test_get_user(client, endpoint, status_code, real_user):
    if real_user:
        result = client.get(endpoint+str(pytest.global_user_id))
    else:
        result = client.get(endpoint)
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "json", "status_code", "real_user"),
    [
        ("/users", {}, 405, False),
        ("/users/0", {
            "username": "pytest",
            "password": "pytest",
            "address": "pytest"
        }, 404, False),
        ("/users/", {
            "username": "pytest",
            "password": "pytest",
            "address": "pytest"
        }, 204, True)
    ]
)
def test_update_user(client, endpoint, json, status_code, real_user):
    if real_user:
        result = client.put(endpoint+str(pytest.global_user_id), json=json)
    else:
        result = client.put(endpoint, json=json)
    assert result.status_code == status_code


@pytest.mark.parametrize(
    ("endpoint", "status_code", "real_delete"),
    [
        ("/users", 405, False),
        ("/users/0", 404, False),
        ("/users/", 204, True),
    ]
)
def test_delete_user(client, endpoint, status_code, real_delete):
    if real_delete:
        result = client.delete(endpoint+str(pytest.global_user_id))
    else:
        result = client.delete(endpoint)
    assert result.status_code == status_code
