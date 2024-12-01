import json

def lambda_handler(event, context):
    name = event["name"]
    password = event["password"]
    message = event["message"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{message} {name}, your password is {password}"
        }),
    }
