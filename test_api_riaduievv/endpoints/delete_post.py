import requests
import allure
from endpoints.Base_endpoint import BaseEndpoint


class DeletePost(BaseEndpoint):
    @allure.feature("Manage API queries")
    @allure.story("Delete product")
    @allure.title("Delete product")
    @allure.step("Run request to delete a post")
    def delete_post(self, post_id):
        self.response = requests.delete(f"{self.url}/{post_id}")
        self.json = self.response.json()
        return self.response
