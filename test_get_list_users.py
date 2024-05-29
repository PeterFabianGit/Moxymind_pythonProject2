import requests
import pytest


def test_get_list_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    assert "id" in data["data"][0]
    assert "email" in data["data"][0]