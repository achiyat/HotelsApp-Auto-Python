# put_first_hotel.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from http import HTTPStatus
from tests.conftest import create_hotels
from faker.generator import random


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Update Hotel")
class TestPutFirstHotel(BaseTest):
    @allure.title("Test updating the first hotel")
    @allure.description("Update the details of the first hotel returned by the API")
    @allure.severity(allure.severity_level.NORMAL)
    def test_put_first_hotel(self, create_hotels):
        allure.attach(
            'This test updates the details of the first hotel returned by the API.',
            'Test Description'
        )
        with allure.step("Retrieve all hotels and get the first hotel's details"):
            first_hotel = self.get_first().json()
            first_hotel_id = first_hotel["id"]

        with allure.step("Modify the rating of the first hotel"):
            first_hotel["rating"] = random.randint(0, 9)

        with allure.step("Send PUT request to update the first hotel"):
            response = self.put_by_id(first_hotel_id, first_hotel)

        with allure.step("Attach the response details as a file"):
            self.create_file_response(response=response)

        with allure.step("Verify the status code and attach the test details as a file"):
            result = self.create_dict_result(
                name="put_first_hotel",
                actual=str(response.status_code),
                expected=str(HTTPStatus.NO_CONTENT),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
