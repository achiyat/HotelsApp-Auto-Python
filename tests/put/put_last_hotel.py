# put_last_hotel.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from http import HTTPStatus
from tests.conftest import create_hotels
from faker.generator import random


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Update Hotel")
class TestPutLastHotel(BaseTest):
    @allure.title("Test updating the rating of the last hotel")
    @allure.description("Update the rating of the last hotel returned by the API")
    @allure.severity(allure.severity_level.NORMAL)
    def test_put_last_hotel(self, create_hotels):
        allure.attach(
            'This test updates the rating of the last hotel returned by the API.',
            'Test Description'
        )

        with allure.step("Retrieve all hotels and get the last hotel's details"):
            last_hotel = self.get_last().json()
            last_hotel_id = last_hotel["id"]

        with allure.step("Modify the rating of the last hotel"):
            last_hotel["rating"] = random.randint(0, 9)

        with allure.step("Send PUT request to update the last hotel"):
            response = self.put_by_id(last_hotel_id, last_hotel)

        with allure.step("Attach the response details as a file"):
            self.create_file_response(response=response)

        with allure.step("Verify the status code and attach the test details as a file"):
            result = self.create_dict_result(
                name="put_last_hotel",
                actual=str(response.status_code),
                expected=str(HTTPStatus.NO_CONTENT),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
