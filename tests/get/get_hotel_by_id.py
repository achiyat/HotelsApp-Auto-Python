# get_hotel_by_id.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from http import HTTPStatus
import pytest

ids = [1, 70]


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Get Hotel")
class TestGetHotelById(BaseTest):
    @allure.title("Test retrieving hotel by ID")
    @allure.description("Retrieve a hotel by its ID and verify the response status code")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("hotel_id", ids)
    def test_get_hotel_by_id(self, hotel_id):
        allure.attach(
            'This test retrieves a hotel by its ID and verifies the response status code.',
            'Test Description'
        )
        with allure.step("Retrieve hotel by ID"):
            response = self.get_by_id(hotel_id)

        with allure.step("Verify the status code and attach the test details as a file"):
            if response.ok:
                result = self.create_dict_result(
                    name="get_hotel_by_id",
                    actual=str(response.status_code),
                    expected=str(HTTPStatus.OK),
                    inequality_symbol=Symbols.EQUAL_TO
                )

                self.create_file_result(result=result)
                assert result["Assert"]

            else:
                result = self.create_dict_result(
                    name="get_hotel_by_id",
                    actual=str(response.status_code),
                    expected=str(HTTPStatus.NOT_FOUND),
                    inequality_symbol=Symbols.EQUAL_TO
                )

                self.create_file_result(result=result)
                assert result["Assert"]
