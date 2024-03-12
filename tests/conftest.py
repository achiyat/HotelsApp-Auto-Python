# conftest.py
import requests
from pytest import fixture
from faker import Faker
from faker.generator import random
from _pytest.config import Config


fake = Faker()


@fixture
# create hotels random data
def create_hotels():
    global fake
    requests.post(
        "http://localhost:8090/example/v1/hotels/",
        json={
            "city": fake.city(),
            "description": fake.text(),
            "name": fake.name(),
            "rating": random.randint(0, 9),
        },
    )


def pytest_configure(config: Config) -> None:
    config.option.allure_report_dir = "allure-results"
