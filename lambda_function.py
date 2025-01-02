def lambda_handler(event, context):
    """
    Example Lambda function that returns 'Hello Sai' when tested.
    """
    return {
        'statusCode': 200,
        'body': 'Hello Sai'
    }
