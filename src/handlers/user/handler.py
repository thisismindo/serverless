import os
import requests

def get_user(event, context):
    # for demonstration purposes always return success with empty body
    return {
        'statusCode': 200,
        'body': {}
    }
