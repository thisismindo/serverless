import os
import requests

def get_order(event, context):
    # for demonstration purposes always return success with empty body
    return {
        'statusCode': 200,
        'body': {}
    }
