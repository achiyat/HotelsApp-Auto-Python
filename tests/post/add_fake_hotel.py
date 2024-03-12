# add_fake_hotel.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from http import HTTPStatus
from faker import Faker
from faker.generator import random
import pytest

fake = Faker()
hotel = [(fake.city(), fake.text(), fake.name(), random.randint(0, 9)),]


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Add Hotel")
class TestAddFakeHotel(BaseTest):
    @allure.title("Test adding a hotel with dynamic data")
    @allure.description("Create dynamic hotel")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("city, description, name, rating", hotel)
    def test_add_fake_hotel(self, city, description, name, rating):
        allure.attach(
            'This test adds a hotel with dynamic data generated using Faker.',
            'Test Description'
        )
        with allure.step("Sending request to add hotel"):
            response = self.add_object(
                {"city": city, "description": description, "name": name, "rating": rating},
                params={"city": city, "description": description, "name": name, "rating": rating}
            )

        with allure.step("Attach the response details as a file"):
            self.create_file_response(response=response)

        with allure.step("Verify the status code and attach the test details as a file"):
            result = self.create_dict_result(
                name="add_fake_hotel",
                actual=str(response.status_code),
                expected=str(HTTPStatus.CREATED),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
