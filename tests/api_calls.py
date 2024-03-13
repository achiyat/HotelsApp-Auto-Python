# api_calls.py
from typing import Type
import requests
from requests import Response
from tests.allure_attachments import AllureAttachments
from tests.common import Get


class ApiRequests:
    """
    wrapper class for api requests that includes built in allure logging.
    """

    @staticmethod
    def get(url: str, _type: Type[Get], params=None) -> Response:
        AllureAttachments.attach_request(url, request_method="GET", q_params=params)
        response = ApiRequests.get_requests(url, _type)
        AllureAttachments.attach_response(response)
        return response

    @staticmethod
    def get_requests(url: str, _type: Type[Get]) -> Response:
        if _type == Get.ALL or _type == Get.BY_ID:
            return requests.get(url)
        elif _type == Get.LAST:
            response_body = requests.get(url).json()
            _id = response_body["content"][len(response_body["content"]) - 1]["id"]
            return requests.get(f"{url}/{_id}")
        elif _type == Get.FIRST:
            _id = requests.get(url).json()["content"][0]["id"]
            return requests.get(f"{url}/{_id}")

    @staticmethod
    def post(url: str, headers=None, data=None, params=None) -> Response:
        AllureAttachments.attach_request(url, request_method="POST", headers=headers, payload=data, q_params=params)
        return requests.post(url, params=params, json=data)

    @staticmethod
    def delete(url: str, params=None) -> Response:
        AllureAttachments.attach_request(url, request_method="DELETE", q_params=params)
        return requests.delete(url, params=params)

    @staticmethod
    def put(url: str, data=None, params=None) -> Response:
        AllureAttachments.attach_request(url, request_method="PUT", payload=data, q_params=params)
        return requests.put(url, params=params, json=data)
