def lambda_handler(event, context):
    """
    Example Lambda function that returns 'Hello World' when tested.
    """
    return {
        'statusCode': 200,
        'body': 'Hello World'
    }
