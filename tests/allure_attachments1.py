# allure_attachments.py
import json
import allure
from allure_commons.types import AttachmentType
from requests import Response
from tests.constant import HEADERS


class AllureAttachments:
    """
    attach allure request, parameters:
    URL
    request method
    headers
    payload
    query parameters
    if payload is None or dictionary we will add to as value to request data dictionary
    else if it's a list we will call to string and encode it as UTF8 string.
    """
    @staticmethod
    def attach_request(url, request_method, headers=None, payload=None, q_params=None) -> None:
        filename = f"[{request_method}] request"
        if isinstance(payload, dict) or payload is None:
            filename += ".json"
            request_data = {
                "RequestMethod": request_method,
                "RequestURL": url,
                "headers": headers,
                "q_params": q_params,
                "payload": payload
            }
            request_data = json.dumps(request_data, indent=4).encode('utf-8')
        elif isinstance(payload, list):
            request_data = payload.__repr__().encode('utf-8')
        else:
            request_data = payload
        allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)

    """
    attach allure request, parameters:
    Response
    filename
    """
    @staticmethod
    def attach_response(res: Response, filename=None) -> None:
        filename = filename or f"response [{res.status_code}]"
        response_data = res.content
        data_type = AllureAttachments.get_attachment_type(res)
        if data_type == AttachmentType.JSON:
            response_data = {
                "URL": res.url,
                "Headers": dict(res.headers),
                "Response": res.json()
            }
            response_data = json.dumps(response_data, indent=4).encode('utf-8')
        elif data_type is None:
            data_type = allure.attachment_type.JSON
            response_data = {
                "URL": res.url,
                "Headers": dict(res.headers),
                "Response": {
                    "Ok": res.ok,
                    "Status code": res.status_code
                }
            }
            response_data = json.dumps(response_data, indent=4).encode('utf-8')
        allure.attach(response_data, name=filename, attachment_type=data_type)

    @staticmethod
    def get_attachment_type(r: Response):
        """
        This function check the content type of the response and
        return the appropriate allure attachment type (from AttachmentType enum)
        :param r: Response object
        :return: AttachmentType value if content_type exist in the list, otherwise, return None
        """
        content_type = r.headers.get('Content-Type', '').split(';')[0]  # split and remove the encoding type
        return next(
            (
                AttachmentType(data.value)
                for data in AttachmentType
                if content_type in data.value
            ),
            None,
        )

    @staticmethod
    def attach_result(result: dict, filename=None) -> None:
        filename = filename or f"attach [{result['Name']}]"
        data_type = allure.attachment_type.JSON
        assert_data = {
            "assert": {
                "result": f"{result['Actual'] == result['Expected']}",
                "Expected": result['Expected'],
                "Actual": result['Actual'],
            }
        }
        response_data = json.dumps(assert_data, indent=4).encode('utf-8')
        allure.attach(response_data, name=filename, attachment_type=data_type)

    # @staticmethod
    # def attach_request_with_assert(response=None, headers=None, payload=None, assert_data=None):
    #     filename = f"[{response.request.method}] request_with_assert"
    #     if isinstance(payload, dict) or payload is None:
    #         filename += ".json"
    #         request_data = {
    #             "RequestMethod": response.request.method,
    #             "RequestURL": response.url,
    #             "headers": HEADERS,
    #             "payload": payload,
    #             "assert": {
    #                 "result": f"{assert_data['Actual']}{assert_data['symbol']}{assert_data['Expected']}",
    #                 "Expected": assert_data['Expected'],
    #                 "Actual": assert_data['Actual'],
    #                 "symbol": assert_data['symbol']
    #             }
    #         }
    #         request_data = json.dumps(request_data, indent=4).encode('utf-8')
    #     elif isinstance(payload, list):
    #         request_data = payload.__repr__().encode('utf-8')
    #     elif isinstance(payload, bytes):
    #         request_data = json.loads(payload.decode('utf-8'))
    #     else:
    #         request_data = payload
    #
    #     allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)
    #


# # 888888888888888888888888888
#
#     @staticmethod
#     def attach_request_with_assert(response=None, headers=None, payload=None, assert_data=None):
#         # # Convert CaseInsensitiveDict to regular dictionary
#         # headers = dict(response.request.headers)
#         #
#         # # Decode bytes payload to string
#         # payload = response.request.body.decode('utf-8')
#
#         filename = f"[{response.request.method}] request_with_assert"
#         if isinstance(payload, dict) or payload is None:
#             filename += ".json"
#             request_data = {
#                 "RequestMethod": response.request.method,
#                 "RequestURL": response.url,
#                 "headers": headers,
#                 "payload": payload,
#                 "assert": {
#                     "result": f"{assert_data['Actual']}{assert_data['symbol']}{assert_data['Expected']}",
#                     "Expected": assert_data['Expected'],
#                     "Actual": assert_data['Actual'],
#                     "symbol": assert_data['symbol']
#                 }
#             }
#             request_data = json.dumps(request_data, indent=4).encode('utf-8')
#         elif isinstance(payload, bytes):
#             request_data = payload.__repr__().encode('utf-8')
#         else:
#             request_data = payload
#
#         allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)
#
#     @staticmethod
#     def attach_request_with_assert(response=None, headers=None, payload=None, assert_data=None):
#         filename = f"[{response.request.method}] request_with_assert.json"
#
#         # Convert CaseInsensitiveDict to regular dictionary
#         headers = dict(response.request.headers)
#
#         # Decode bytes payload to string
#         payload = response.request.body.decode('utf-8')
#
#         request_data = {
#             "RequestMethod": response.request.method,
#             "RequestURL": response.url,
#             "headers": headers,
#             "payload": payload,
#             "assert": {
#                 "result": f"{assert_data['Actual']}{assert_data['symbol']}{assert_data['Expected']}",
#                 "Expected": assert_data['Expected'],
#                 "Actual": assert_data['Actual'],
#                 "symbol": assert_data['symbol']
#             }
#         }
#         request_data = json.dumps(request_data, indent=4).encode('utf-8')
#         allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)
#
#     # @staticmethod
#     # def attach_request_with_assert(response=None, headers=None, payload=None, assert_data=None):
#     #     filename = f"[{response.request.method}] request_with_assert.json"
#     #
#     #     # Convert CaseInsensitiveDict to regular dictionary
#     #     headers = dict(response.request.headers)
#     #
#     #     # Decode bytes payload to string
#     #     payload = response.request.body.decode('utf-8')
#     #
#     #     request_data = {
#     #         "RequestMethod": response.request.method,
#     #         "RequestURL": response.url,
#     #         "headers": headers,
#     #         "payload": payload,
#     #         "assert": {
#     #             "result": f"{assert_data['Actual']}{assert_data['symbol']}{assert_data['Expected']}",
#     #             "Expected": assert_data['Expected'],
#     #             "Actual": assert_data['Actual'],
#     #             "symbol": assert_data['symbol']
#     #         }
#     #     }
#     #     request_data = json.dumps(request_data, indent=4).encode('utf-8')
#     #     allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)
#
#     # @staticmethod
#     # def attach_request_with_assert(response=None, assert_data=None):
#     #     filename = f"[{response.request.method}] request_with_assert.json"
#     #     request_data = {
#     #         "RequestMethod": response.request.method,
#     #         "RequestURL": response.url,
#     #         "headers": response.request.headers,
#     #         "payload": response.request.body,
#     #         "assert": {
#     #             "result": f"{assert_data['Actual']}{assert_data['symbol']}{assert_data['Expected']}",
#     #             "Expected": assert_data['Expected'],
#     #             "Actual": assert_data['Actual'],
#     #             "symbol": assert_data['symbol']
#     #         }
#     #     }
#     #     request_data = json.dumps(request_data, indent=4).encode('utf-8')
#     #     allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)
#
#
#
#     @staticmethod
#     def attach_request_with_assert(response=None, headers=None, payload=None, assert_data=None):
#         filename = f"[{response.request.method}] request_with_assert"
#         if isinstance(payload, dict) or payload is None:
#             filename += ".json"
#             request_data = {
#                 "RequestMethod": response.request.method,
#                 "RequestURL": response.url,
#                 "headers": headers,
#                 "payload": payload,
#                 "assert": {
#                     "result": f"{assert_data['Actual']}{assert_data['symbol']}{assert_data['Expected']}",
#                     "Expected": assert_data['Expected'],
#                     "Actual": assert_data['Actual'],
#                     "symbol": assert_data['symbol']
#                 }
#             }
#             request_data = json.dumps(request_data, indent=4).encode('utf-8')
#         elif isinstance(payload, list):
#             request_data = payload.__repr__().encode('utf-8')
#         elif isinstance(payload, bytes):
#             request_data = json.loads(payload.decode('utf-8'))
#         else:
#             request_data = payload
#
#         allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_request_with_assert(response=None, assert_data=None):
        filename = f"[{response.request.method}] request_with_assert.json"

        # Convert CaseInsensitiveDict to regular dictionary
        # headers = dict(response.request.headers)
        headers = HEADERS

        # Decode bytes payload to string
        payload = response.request.body.decode('utf-8')

        request_data = {
            "RequestMethod": response.request.method,
            "RequestURL": response.url,
            "headers": headers,
            "payload": payload,
            "assert": {
                "result": f"{assert_data['Actual']}{assert_data['symbol']}{assert_data['Expected']}",
                "Expected": assert_data['Expected'],
                "Actual": assert_data['Actual'],
                "symbol": assert_data['symbol']
            }
        }
        request_data = json.dumps(request_data, indent=4).encode('utf-8')
        allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_request1(response, q_params=None) -> None:
        payload = response.request.body
        filename = f"[{response.request.method}] request"
        if isinstance(payload, dict) or payload is None:
            filename += ".json"
            request_data = {
                "RequestMethod": response.request.method,
                "RequestURL": response.url,
                "headers": dict(response.request.headers),
                "q_params": q_params,
                "payload": payload
            }
            request_data = json.dumps(request_data, indent=4).encode('utf-8')
        elif isinstance(payload, list):
            request_data = payload.__repr__().encode('utf-8')
        else:
            request_data = payload
        allure.attach(request_data, name=filename, attachment_type=allure.attachment_type.JSON)
