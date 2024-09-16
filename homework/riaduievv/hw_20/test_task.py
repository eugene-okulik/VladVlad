import requests
import pytest
import allure


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
@allure.feature("Manage API queries")
@allure.story("Create post with different data")
@allure.title("Create product")
def test_add_object(body, start_end_test, before_after_test):
    with allure.step("Prepare test data"):
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
    with allure.step("Run request to create a post"):
        response = requests.post(
            "https://api.restful-api.dev/objects", json=body, headers=headers
        )
    with allure.step("Check status code is 200"):
        assert response.status_code == 200


allure.feature("Manage API queries")
allure.story("Updating product information")


@allure.title("Change product information")
@pytest.mark.critical
def test_put_object(new_post_id, before_after_test):
    with allure.step("Prepare data to update product information"):
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
    with allure.step("Run request with updated information"):
        response = requests.put(
            f"https://api.restful-api.dev/objects/{new_post_id}",
            headers=headers,
            json=body,
        ).json()
    with allure.step("Check color is silver"):
        assert response["data"]["color"] == "silver"


allure.feature("Manage API queries")
allure.story("Partly updating product information")


@allure.title("Partly change product information")
@pytest.mark.medium
def test_partialy_update_object(new_post_id, before_after_test):
    with allure.step("Prepare data to partly update product information"):
        body = {"name": "Apple MacBook Pro (Updated Name)"}
        headers = {"Content-type": "application/json"}
    with allure.step("Run request with partly updated information"):
        response = requests.patch(
            f"https://api.restful-api.dev/objects/{new_post_id}",
            headers=headers,
            json=body,
        ).json()
    with allure.step("Check name is changed"):
        assert response["name"] == "Apple MacBook Pro (Updated Name)"


allure.feature("Manage API queries")
allure.story("Delete product")


@allure.title("Delete product")
def test_delete_object(new_post_id, before_after_test):
    with allure.step("Run request to delete a post"):
        response = requests.delete(f"https://api.restful-api.dev/objects/{new_post_id}")
    with allure.step("Check status code is 200"):
        assert response.status_code == 200
