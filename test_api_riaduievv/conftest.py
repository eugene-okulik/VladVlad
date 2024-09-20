import pytest
from endpoints.create_post import CreatePost
import requests

from endpoints.partially_update_post import PartiallyUpdatePost
from endpoints.update_post import UpdatePost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def create_endpoint():
    return CreatePost()


@pytest.fixture()
def update_endpoint():
    return UpdatePost()


@pytest.fixture()
def partially_update_endpoint():
    return PartiallyUpdatePost()


@pytest.fixture()
def delete_endpoint():
    return DeletePost()


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
    print("\nTesting completed")


@pytest.fixture()
def before_after_test():
    print("before test")
    yield
    print("\nafter test")
