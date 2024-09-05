import requests
import pytest


@pytest.fixture()
def new_post_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    }
    headers = {"Content-type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects", headers=headers, json=body
    )
    post_id = response.json()["id"]
    yield post_id
    requests.delete(f"https://api.restful-api.dev/objects/{post_id}")


@pytest.fixture(scope="session")
def start_end_test():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def before_after_test():
    print("before test")
    yield
    print("\nafter test")


@pytest.mark.parametrize(
    "body",
    [
        {
            "name": "Apple MacBook",
            "data": {
                "year": 2024,
                "price": 900,
                "CPU model": "M1",
                "Hard disk size": "1 TB",
            },
        },
        {"name": "Dell XPS 15"},
        {"data": {"year": 2021, "price": 1399.99, "CPU model": "Intel Core i5"}},
    ],
)
def test_add_object(body, start_end_test, before_after_test):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    }
    headers = {"Content-type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects", json=body, headers=headers
    )
    assert response.status_code == 200


@pytest.mark.critical
def test_put_object(new_post_id, before_after_test):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver",
        },
    }
    headers = {"Content-type": "application/json"}
    response = requests.put(
        f"https://api.restful-api.dev/objects/{new_post_id}", headers=headers, json=body
    ).json()
    assert response["data"]["color"] == "silver"


@pytest.mark.medium
def test_partialy_update_object(new_post_id, before_after_test):
    body = {"name": "Apple MacBook Pro (Updated Name)"}
    headers = {"Content-type": "application/json"}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{new_post_id}", headers=headers, json=body
    ).json()
    assert response["name"] == "Apple MacBook Pro (Updated Name)"


def test_delete_object(new_post_id, before_after_test):
    response = requests.delete(f"https://api.restful-api.dev/objects/{new_post_id}")
    assert response.status_code == 200
