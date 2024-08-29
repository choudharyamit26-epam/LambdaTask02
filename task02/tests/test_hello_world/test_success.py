from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        # Mock event and context
        mock_event = {
            'requestContext': {
                'http': {
                    'method': 'GET',
                    'path': '/hello'
                }
            }
        }
        mock_context = {}

        # Expected output
        expected_response = '{"statusCode": 200, "message": "Hello from Lambda"}'

        # Run the test
        actual_response = self.HANDLER.lambda_handler(mock_event, mock_context)
        self.assertEqual(actual_response, expected_response)
