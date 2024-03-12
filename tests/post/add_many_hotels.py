# add_many_hotels.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from http import HTTPStatus
import pytest

data = [
    ("New York", "A luxurious hotel located in the heart of Manhattan.", "Grand Hotel", 9),
    ("Los Angeles", "A modern hotel with stunning views of the city skyline.", "Sunset Inn", 8),
]


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Add Hotel")
class TestAddManyHotels(BaseTest):
    @allure.title("Test adding multiple hotels")
    @allure.description("Create 2 hotels")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("city, description, name, rating", data)
    def test_add_many_hotels(self, city, description, name, rating):
        allure.attach(
            'This test adds multiple hotels with predefined data.',
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
                name="add_many_hotels",
                actual=str(response.status_code),
                expected=str(HTTPStatus.CREATED),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
