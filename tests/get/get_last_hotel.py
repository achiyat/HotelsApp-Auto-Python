# get_last_hotel.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from tests.conftest import create_hotels


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Get Hotel")
class TestGetLastHotel(BaseTest):
    @allure.title("Test retrieving the last hotel")
    @allure.description("Retrieve the last hotel and verify its ID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_last_hotel(self, create_hotels):
        allure.attach(
            'This test retrieves the last hotel and verifies its ID.',
            'Test Description'
        )
        with allure.step("Retrieve all hotels"):
            response_body = self.get_all().json()
            res_object_id = self.get_last_object(response_body, "content")["id"]

        with allure.step("Get ID of the last hotel"):
            last_hotel_id = self.get_last().json()["id"]

        with allure.step("Verify last hotel ID and attach the test details as a file"):
            result = self.create_dict_result(
                name="get_last_hotel",
                actual=str(res_object_id),
                expected=str(last_hotel_id),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
