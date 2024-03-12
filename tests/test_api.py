# test_api.py
import time
from http import HTTPStatus
import requests
from faker import Faker
from faker.generator import random
from constant import BASE_URL, HEADERS
import pytest


data = [
    (1, HTTPStatus.OK),
]


def test_get_hotels(create_hotels):
    response = requests.get(BASE_URL)
    assert response.status_code == HTTPStatus.OK
    assert "application/json" in response.headers["Content-Type"]
    response_body = response.json()
    assert response_body["totalElements"] > 0


def test_get_hotel_by_id():
    response = requests.get(f"{BASE_URL}/2")
    response_body = response.json()
    assert response_body["name"] == "Hotel_111"


def test_not_found_hotel_by_id():
    response = requests.get(f"{BASE_URL}/2")
    print(HTTPStatus.NOT_FOUND)
    print(response.status_code)
    assert response.status_code == 404


@pytest.mark.parametrize("hotel_id, response_code", data)
def test_data_provider(hotel_id, response_code):
    response = requests.get(f"{BASE_URL}/{hotel_id}")
    assert response.status_code == response_code


def test_add_hotel():
    fake = Faker()
    response = requests.post(
        BASE_URL,
        json={
            "city": fake.city(),
            "description": fake.text(),
            "name": fake.name(),
            "rating": random.randint(0, 9),
        },
    )
    assert response.status_code == HTTPStatus.CREATED


def test_put_rating():
    hotel_id = 9
    response = requests.get(f"{BASE_URL}/{hotel_id}")
    response_body = response.json()
    rating = response_body["rating"]
    print(rating)
    response_body["rating"] = 8
    response = requests.put(f"{BASE_URL}/{hotel_id}", json=response_body, headers=HEADERS)
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_all_hotels(create_hotels):
    response_body = requests.get(BASE_URL).json()
    list_id = [hotel["id"] for hotel in response_body["content"]]

    for hotel in list_id:
        requests.delete(f"{BASE_URL}/{hotel}")

    response = requests.get(BASE_URL)
    assert response.status_code == HTTPStatus.OK

    response_body = response.json()
    assert response_body["totalElements"] == 0
