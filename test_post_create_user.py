import requests
import pytest


def test_post_create_user():
    url = "https://reqres.in/api/users"
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url, json=user_data)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
