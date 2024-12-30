import boto3

def lambda_handler(event, context):
    """
    Example Lambda function that fetches information about EC2 instances.
    """
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    return {
        'statusCode': 200,
        'body': response
    }
