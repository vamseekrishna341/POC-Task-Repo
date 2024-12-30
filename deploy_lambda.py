import boto3
import sys

def update_lambda_function(function_name, zip_file):
    """
    Updates the AWS Lambda function code.
    """
    client = boto3.client('lambda')
    with open(zip_file, 'rb') as f:
        zip_data = f.read()
    response = client.update_function_code(
        FunctionName=function_name,
        ZipFile=zip_data
    )
    print(f"Updated Lambda function: {function_name}")
    return response

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python deploy_lambda.py <function_name> <zip_file>")
        sys.exit(1)
    function_name = sys.argv[1]
    zip_file = sys.argv[2]
    update_lambda_function(function_name, zip_file)
