import json
from generate_random_password import generate_random_password


def lambda_handler(event, context):

    passwords = generate_random_password(20, 10, True, True)
    response = json.dumps(passwords)

    return {
        'statusCode': 200,
        'statusMessage': "SUCCESS",
        'body': json.dumps(response)
    }
