import requests
import pytest


def test_get_list_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200, "Status code is not 200"

    data = response.json()

    # Assert the 'total' key is present and has a value
    assert "total" in data, "'total' key is missing in response"
    total = data["total"]
    assert total > 0, "'total' value is not greater than 0"

    # Assert 'data' key is present and has a list of users
    assert "data" in data, "'data' key is missing in response"
    users = data["data"]
    assert isinstance(users, list), "'data' is not a list"
    assert len(users) > 0, "No users found in 'data'"

    # Assert 'last_name' for the first and second users in 'data'
    if len(users) > 1:
        first_user_last_name = users[0]["last_name"]
        second_user_last_name = users[1]["last_name"]
        assert isinstance(first_user_last_name, str) and len(
            first_user_last_name) > 0, "First user's last name is invalid"
        assert isinstance(second_user_last_name, str) and len(
            second_user_last_name) > 0, "Second user's last name is invalid"
    else:
        pytest.fail("Less than 2 users found in 'data'")

    # Count the number of received users in 'data' and compare with 'total'
    received_users_count = len(users)
    assert received_users_count <= total, f"Received users count ({received_users_count}) is greater than 'total' ({total})"

