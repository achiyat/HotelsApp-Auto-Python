# put_hotel_by_id.py
from http import HTTPStatus
from tests.base_test import BaseTest
import pytest
import allure
from tests.common import Symbols

data = [
    ("Dubai", "An extravagant hotel overlooking the stunning Dubai skyline.", "Desert Oasis Resort", 9)
]

new_hotel = {
    "city": "Paris",
    "description": "A charming hotel in the romantic city of Paris.",
    "name": "Eiffel Tower Hotel",
    "rating": 10
}


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Update Hotel")
class TestPutHotelById(BaseTest):
    @allure.title("Test updating a hotel by ID")
    @allure.description("Update a hotel by ID")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("city, description, name, rating", data)
    def test_put_hotel_by_id(self, city, description, name, rating):
        allure.attach(
            'This test updates a hotel by ID.',
            'Test Description'
        )

        with allure.step("Add a new hotel"):
            response = self.add_object(
                {"city": city, "description": description, "name": name, "rating": rating},
                params={"city": city, "description": description, "name": name, "rating": rating}
            )
            self.create_file_response(response=response)

        with allure.step("Get the ID of the last hotel"):
            last_hotel_id = self.get_last().json()["id"]
            new_hotel["id"] = last_hotel_id

        with allure.step("Send PUT request to update the hotel by ID"):
            response = self.put_by_id(last_hotel_id, new_hotel)

        with allure.step("Attach the response details as a file"):
            self.create_file_response(response=response)

        with allure.step("Verify the status code and attach the test details as a file"):
            result = self.create_dict_result(
                name="put_hotel_by_id",
                actual=str(response.status_code),
                expected=str(HTTPStatus.NO_CONTENT),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
