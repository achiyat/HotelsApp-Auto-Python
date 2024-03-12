# get_first_hotel.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from tests.conftest import create_hotels


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Get Hotel")
class TestGetFirstHotel(BaseTest):
    @allure.title("Test retrieving the first hotel")
    @allure.description("Retrieve the first hotel and verify its ID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_first_hotel(self, create_hotels):
        allure.attach(
            'This test retrieves the first hotel and verifies its ID.',
            'Test Description'
        )
        with allure.step("Retrieve all hotels"):
            response_body = self.get_all().json()
            res_object_id = self.get_first_object(response_body, "content")["id"]

        with allure.step("Get ID of the first hotel"):
            first_hotel_id = self.get_first().json()["id"]

        with allure.step("Verify first hotel ID and attach the test details as a file"):
            result = self.create_dict_result(
                name="get_first_hotel",
                actual=str(res_object_id),
                expected=str(first_hotel_id),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
