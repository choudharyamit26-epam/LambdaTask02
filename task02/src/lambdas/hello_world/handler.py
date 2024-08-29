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
        print("=====>>>", event.httpMethod, event.path)
        return {
            "statusCode": 200,
            "headers": "application/json",
            "message": "Hello from Lambda"
        }


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
