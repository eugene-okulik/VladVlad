import pytest


TEST_DATA_PARAM = [
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    },
    {"name": "Dell XPS 15"},
    {"data": {"year": 2021, "price": 1399.99, "CPU model": "Intel Core i5"}},
]


@pytest.mark.parametrize("data", TEST_DATA_PARAM)
def test_add_object(create_endpoint, data, start_end_test, before_after_test):
    create_endpoint.new_post(body=data)
    create_endpoint.check_response_status_code_is_200()


@pytest.mark.critical
def test_put_object(update_endpoint, new_post_id, before_after_test):
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
    update_endpoint.update_created_post(body=body, post_id=new_post_id)
    update_endpoint.check_response_color_is_silver()


@pytest.mark.medium
def test_partially_update_object(
    partially_update_endpoint, new_post_id, before_after_test
):
    body = {"name": "Apple MacBook Pro (Updated Name)"}
    partially_update_endpoint.partially_update_created_post(
        body=body, post_id=new_post_id
    )
    partially_update_endpoint.check_name_is_changed()


def test_delete_object(delete_endpoint, new_post_id, before_after_test):
    delete_endpoint.delete_post(post_id=new_post_id)
    delete_endpoint.check_response_status_code_is_200()
