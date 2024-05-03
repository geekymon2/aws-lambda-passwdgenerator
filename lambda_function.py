import json
from generate_random_password import generate_random_password


def lambda_handler(event, context):

    passwords = generate_random_password(int(event['length']), int(event['count']), bool(event['digits']),
                                         bool(event['special_chars']))
    response = json.dumps(passwords)

    return {
        'statusCode': 200,
        'statusMessage': "SUCCESS",
        'body': json.dumps(response)
    }
