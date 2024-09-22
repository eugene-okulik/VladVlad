import requests
import allure
from endpoints.Base_endpoint import BaseEndpoint


class CreatePost(BaseEndpoint):
    @allure.feature("Manage API queries")
    @allure.story("Create post with different data")
    @allure.title("Create product")
    @allure.step("Run request to create a post")
    def new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response
