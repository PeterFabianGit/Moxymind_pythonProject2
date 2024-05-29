import requests
import pytest
import json
import time

# Load test data from external source
with open('user_data.json') as f:
    user_data = json.load(f)

@pytest.mark.parametrize("user", user_data)
def test_post_create_user(user):
    url = "https://reqres.in/api/users"
    start_time = time.time()
    response = requests.post(url, json=user)
    end_time = time.time()

    response_time = (end_time - start_time) * 100  # Convert to milliseconds

    assert response.status_code == 201, "Status code is not 201"

    data = response.json()
    assert "id" in data, "'id' key is missing in response"
    assert "createdAt" in data, "'createdAt' key is missing in response"
    # assert data["name"] == "morpheus"
    # assert data["job"] == "leader"

    # Assert that the response time was less than 100 ms
    assert response_time < 100, f"Response time ({response_time} ms) exceeded the limit (100 ms)"
