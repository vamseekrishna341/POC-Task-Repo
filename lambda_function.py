import json
 
def lambda_handler(event, context):
    """
    Lambda function that returns a greeting and performs a simple arithmetic operation.
    """
    # Get the name from the event, default to 'World' if not provided
    name = event.get('name', 'World')
    # Get numbers and operation from the event, with defaults
    num1 = event.get('num1', 20)
    num2 = event.get('num2', 6)
    operation = event.get('operation', 'add')
 
    # Perform the arithmetic operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Error: Invalid operation"
 
    # Prepare the response
    response = {
        'greeting': f'Hello {name}',
        'arithmetic_result': f"Result of {operation} operation on {num1} and {num2} is: {result}"
    }
 
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
