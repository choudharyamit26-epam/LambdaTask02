from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.lambda_handler(dict(), dict()), {
         "statusCode": 200,
         "message": "Hello from Lambda"
     })

