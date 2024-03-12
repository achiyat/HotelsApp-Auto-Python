# get_all_hotels.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from tests.conftest import create_hotels


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Get Hotel")
class TestGetAllHotels(BaseTest):
    @allure.title("Test retrieving all hotels")
    @allure.description("Retrieve all hotels and verify the response status code")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_all_hotels(self, create_hotels):
        allure.attach(
            'This test retrieves all hotels and verifies the response status code.',
            'Test Description'
        )
        with allure.step("Retrieve all hotels"):
            response_body = self.get_all().json()

        with allure.step("Verify the total elements and attach the test details as a file"):
            result = self.create_dict_result(
                name="get_all_hotels",
                actual=str(response_body["totalElements"]),
                expected=str(0),
                inequality_symbol=Symbols.GREATER_THAN
            )

            self.create_file_result(result=result)
            assert result["Assert"]
