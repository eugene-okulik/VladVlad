import requests
import allure
from endpoints.Base_endpoint import BaseEndpoint


class PartiallyUpdatePost(BaseEndpoint):
    @allure.feature("Manage API queries")
    @allure.story("Partially updating product information")
    @allure.title("Partially change product information")
    @allure.step("Run request with partially updated information")
    def partially_update_created_post(self, body, post_id, headers=None):
        headers = headers if headers else self.headers

        self.response = requests.patch(
            f"{self.url}/{post_id}", json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step("Check name is changed")
    def check_name_is_changed(self, name):
        assert self.json["name"] == name
