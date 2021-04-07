import json

def lambda_handler(event, context):

    httpMethod = event.httpMethod
    httpPath = event.path

    if( httpMethod == 'GET' and httpPath == 'hello'):
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world",
                # "location": ip.text.replace("\n", "")
            }),
        }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "others",
                # "location": ip.text.replace("\n", "")
            }),
        }