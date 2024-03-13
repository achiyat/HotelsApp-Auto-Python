# base_test.py
import requests
from requests import Response
from tests.allure_attachments import AllureAttachments
from tests.api_calls import ApiRequests
from tests.common import Get
from tests.constant import BASE_URL, HEADERS
from typing import Type
from tests.common import Symbols


class BaseTest:
    @staticmethod
    def get_all() -> Response:
        return ApiRequests.get(BASE_URL, Get.ALL, params="All Objects")

    @staticmethod
    def get_first() -> Response:
        return ApiRequests.get(BASE_URL, Get.FIRST, params="First Object")

    @staticmethod
    def get_last() -> Response:
        return ApiRequests.get(BASE_URL, Get.LAST, params="Last Object")

    @staticmethod
    def get_by_id(_id: int | str) -> Response:
        return ApiRequests.get(
            f"{BASE_URL}/{_id}",
            Get.BY_ID,
            params={"id": _id}
        )

    @staticmethod
    def add_object(_dict: dict, params=None) -> Response:
        return ApiRequests.post(
            BASE_URL,
            headers=HEADERS,
            data=_dict,
            params=params
        )

    @staticmethod
    def put_by_id(_id: int | str, data: dict | list) -> Response:
        return ApiRequests.put(
            f"{BASE_URL}/{_id}",
            data=data,
            params={"id": _id}
        )

    @staticmethod
    def delete_by_id(_id: int | str) -> Response:
        return ApiRequests.delete(
            f"{BASE_URL}/{_id}",
            params={"id": _id}
        )

    # change it
    @staticmethod
    def delete_all(_list: list):
        for hotel_id in _list:
            requests.delete(f"{BASE_URL}/{hotel_id}")

    @staticmethod
    def get_value_from_list(_list: list, inx: int) -> any:
        return _list[inx]

    @staticmethod
    def get_value_from_dict(dictionary: dict, key: str | int) -> any:
        return dictionary.get(key)

    @staticmethod
    def get_first_object(_dict: dict, key: str | int) -> any:
        _list = BaseTest.get_value_from_dict(_dict, key)
        return BaseTest.get_value_from_list(_list, 0)

    @staticmethod
    def get_last_object(_dict: dict | Response, key: str | int) -> any:
        _list = BaseTest.get_value_from_dict(_dict, key)
        return BaseTest.get_value_from_list(_list, (len(_list) - 1))

    @staticmethod
    def create_file_response(response: Response, filename=None) -> None:
        AllureAttachments.attach_response(response, filename)

    @staticmethod
    def create_file_result(result: dict, filename=None) -> None:
        AllureAttachments.attach_result(result, filename)

    @staticmethod
    def create_dict_result(name: str, actual: str, expected: str, inequality_symbol: Type[Symbols]) -> dict:
        match inequality_symbol:
            case Symbols.EQUAL_TO:
                result = actual == expected
            case Symbols.NOT_EQUAL_TO:
                result = actual != expected
            case Symbols.GREATER_THAN:
                result = actual > expected
            case Symbols.LESS_THAN:
                result = actual < expected
            case _:
                raise ValueError("Invalid inequality symbol provided.")

        return {
            "Name": name,
            "Actual": actual,
            "Expected": expected,
            "Assert": result,
            "result": f"{actual} {inequality_symbol} {expected}",
        }
