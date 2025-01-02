import json

def lambda_handler(event, context):
    """
    Lambda function to handle API Gateway requests.

    Args:
        event (dict): The event payload containing the request data.
        context (LambdaContext): Information about the invocation, function, and runtime environment.

    Returns:
        dict: HTTP response with status code and body.
    """
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from Lambda!",
            "input": event
        })
    }
