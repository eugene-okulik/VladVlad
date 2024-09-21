import requests
import allure
from endpoints.Base_endpoint import BaseEndpoint


class UpdatePost(BaseEndpoint):
    @allure.feature("Manage API queries")
    @allure.story("Updating product information")
    @allure.title("Change product information")
    @allure.step("Run request with updated information")
    def update_created_post(self, body, post_id, headers=None):
        headers = headers if headers else self.headers

        self.response = requests.put(
            f"{self.url}/{post_id}", json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step("Check color is silver")
    def check_response_color_is_silver(self, color):
        assert self.json["data"]["color"] == color
