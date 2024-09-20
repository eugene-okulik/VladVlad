import allure


class BaseEndpoint:
    url = "https://api.restful-api.dev/objects"
    response = None
    json = None
    headers = {"Content-type": "application/json"}

    @allure.step("Check status code is 200")
    def check_response_status_code_is_200(self):
        assert self.response.status_code == 200
