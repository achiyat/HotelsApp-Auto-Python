# add_multiple_hotels.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from http import HTTPStatus
from faker import Faker
from faker.generator import random
import pytest


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Add Hotel")
class TestAddMultipleHotels(BaseTest):
    @allure.title("Test adding multiple dynamic hotels")
    @allure.description("Create 50 dynamic hotels")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.repeat(3, timeout=30)
    def test_add_multiple_hotels(self):
        allure.attach(
            'This test adds multiple hotels with dynamic data generated using Faker.',
            'Test Description'
        )
        fake = Faker()
        hotel = {"city": fake.city(), "description": fake.text(), "name": fake.name(), "rating": random.randint(0, 9)}
        with allure.step("Sending request to add hotel"):
            response = self.add_object(
                hotel,
                params=hotel
            )

        with allure.step("Attach the response details as a file"):
            self.create_file_response(response=response)

        with allure.step("Verify the status code and attach the test details as a file"):
            result = self.create_dict_result(
                name="add_multiple_hotels",
                actual=str(response.status_code),
                expected=str(HTTPStatus.CREATED),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
