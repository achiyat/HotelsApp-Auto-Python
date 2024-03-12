# allure_attachments.py
import json
import allure
from allure_commons.types import AttachmentType
from requests import Response


class AllureAttachments:
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
    def get_attachment_type(r: Response) -> AttachmentType | None:
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
                "Actual": result['Actual'],
                "Expected": result['Expected'],
                "Assert": result['Assert'],
                "result": result['result'],
            }
        }
        response_data = json.dumps(assert_data, indent=4).encode('utf-8')
        allure.attach(response_data, name=filename, attachment_type=data_type)

    # @staticmethod
    # def get_inequality_symbols(actual: str, expected: str) -> str:
    #     if actual == expected:
    #         return f"{actual} == {expected}"
    #     elif actual != expected:
    #         return f"{actual} != {expected}"
    #     elif actual > expected:
    #         return f"{actual} > {expected}"
    #     elif actual < expected:
    #         return f"{actual} < {expected}"
