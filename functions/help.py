import json


def handle(event, context):
    help_info="""
    Usage: /bot-<command>

    where <command> is one of :
        help, scale-out

    /bot-help           Provides help information about how to use bot
    /bot-scale-out      Provides a way to scale out infrastructure (in development)


    """


    body = {
        "message": help_info,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": help_info
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
