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
        http_method = event.get('requestContext', {}).get('http', {}).get('method')
        path = event.get('requestContext', {}).get('http', {}).get('path')

        print(f"HTTP Method: {http_method}, Path: {path}")
        print("=========>", event)
        print("<<<=========>", context)
        if http_method == 'GET' and path == "/hello":
            return json.dumps({
                "statusCode": 200,
                "message": "Hello from Lambda"
            })
        else:
            return json.dumps({
                "statusCode": 400,
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {http_method}"
            })


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
