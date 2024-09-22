from locust import task, HttpUser
import random


class ApiTest(HttpUser):
    headers = {"Content-type": "application/json; charset=UTF-8"}

    @task(1)
    def get_objects(self):
        self.client.get("/posts")

    @task(1)
    def add_object(self):
        data = {
            "title": "foo",
            "body": "bar",
            "userId": 1,
        }
        self.client.post("/posts", headers=self.headers, json=data)

    @task(2)
    def update_object(self):
        data = {
            "id": 1,
            "title": "foo",
            "body": "bar",
            "userId": 1,
        }
        self.client.put("/posts/1", headers=self.headers, json=data)

    @task(2)
    def patch_object(self):
        data = {"title": "hw21"}
        self.client.patch(
            f"/posts/{random.choice([1,9,13,14])}", headers=self.headers, json=data
        )

