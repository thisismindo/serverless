import os
import requests
from random import randrange
from src.services.user.user_service import UserService

USER_SERVICE = UserService()

def get_user(event, context):
    # for demonstration purposes always return
    # success with static fetch user response
    return {
        'statusCode': 200,
        'body': USER_SERVICE.fetch_user(user_id=randrange(1,100))
    }
