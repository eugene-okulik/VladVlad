import requests


def create_object():
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
    return response.json()["id"]


def clear(post_id):
    requests.delete(f"https://api.restful-api.dev/objects/{post_id}")


def add_object():
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


add_object()


def put_object():
    post_id = create_object()
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
        f"https://api.restful-api.dev/objects/{post_id}", headers=headers, json=body
    ).json()
    assert response["data"]["color"] == "silver"
    clear(post_id)


put_object()


def partialy_update_object():
    post_id = create_object()
    body = {"name": "Apple MacBook Pro (Updated Name)"}
    headers = {"Content-type": "application/json"}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{post_id}", headers=headers, json=body
    ).json()
    assert response["name"] == "Apple MacBook Pro (Updated Name)"
    clear(post_id)


partialy_update_object()


def delete_object():
    post_id = create_object()
    response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
    assert response.status_code == 200


delete_object()
