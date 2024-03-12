# delete_all_hotels.py
import allure
from tests.base_test import BaseTest
from tests.common import Symbols
from tests.conftest import create_hotels


@allure.epic("Hotel Management")
@allure.feature("Hotel CRUD")
@allure.story("Delete Hotel")
class TestDeleteAllHotels(BaseTest):
    @allure.title("Test deleting all hotels")
    @allure.description("Delete all hotels and verify that they have been deleted")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_all_hotels(self, create_hotels):
        allure.attach(
            'This test deletes all hotels and verifies that they have been successfully deleted.',
            'Test Description'
        )
        with allure.step("Retrieve all hotels"):
            response_body = self.get_all().json()
            list_ids = [hotel["id"] for hotel in response_body["content"]]

        with allure.step("Delete all hotels and Retrieve all hotels after deletion"):
            self.delete_all(list_ids)
            response_body = self.get_all().json()

        with allure.step("Verify deletion and attach the test details as a file"):
            result = self.create_dict_result(
                name="delete_all_hotels",
                actual=str(response_body["totalElements"]),
                expected=str(0),
                inequality_symbol=Symbols.EQUAL_TO
            )

            self.create_file_result(result)
            assert result["Assert"]
