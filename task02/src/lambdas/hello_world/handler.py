import json

from commons.abstract_lambda import AbstractLambda
from commons.log_helper import get_logger

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def lambda_handler(self, event, context):
        """
        Explain incoming event here
        """
        # print("=====>>>", event.get("httpMethod"), event.get("path"))
        print("=====>>>", event)
        # if event.get("httpMethod") == "GET" and event.get("path") == "/hello":
        return {
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "statusCode": 200,
                "message": "Hello from Lambda"
            })
        }
        # else:
        #     return {
        #         "headers": {
        #             "Content-Type": "application/json"
        #         },
        #         "body": json.dumps({
        #             "statusCode": 400,
        #             "message": "Bad request syntax or unsupported method"
        #         })
        #     }


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
