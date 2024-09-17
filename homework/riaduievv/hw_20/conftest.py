import pytest
import requests


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
    print(post_id)
    yield post_id
    requests.delete(f"https://api.restful-api.dev/objects/{post_id}")


@pytest.fixture(scope="session")
def start_end_test():
    print("Start testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def before_after_test():
    print("before test")
    yield
    print("\nafter test")
