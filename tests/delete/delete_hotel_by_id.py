# delete_hotel_by_id.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from tests.conftest import create_hotels


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Delete Hotel")
class TestDeleteHotelById(BaseTest):
    @allure.title("Test deleting a hotel by ID")
    @allure.description("Delete a hotel by ID and verify its deletion")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_hotel_by_id(self, create_hotels):
        allure.attach(
            'This test deletes a hotel by its ID and verifies that the deletion was successful.',
            'Test Description'
        )
        with allure.step("Get ID of the last hotel"):
            last_hotel_id = self.get_last().json()["id"]

        with allure.step("Delete hotel by ID"):
            self.delete_by_id(last_hotel_id)

        with allure.step("Retrieve all hotels after deletion"):
            response_body = self.get_all().json()
            res_object_id = self.get_last_object(response_body, "content")["id"]

        with allure.step("Verify deletion and attach the test details as a file"):
            result = self.create_dict_result(
                name="delete_hotel_by_id",
                actual=str(res_object_id),
                expected=str(last_hotel_id),
                inequality_symbol=Symbols.NOT_EQUAL_TO
            )

            self.create_file_result(result=result)
            assert result["Assert"]
