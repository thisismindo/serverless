"""User Service
"""
class UserService:
    def fetch_user(self, user_id):
        return {
            'user': {
                'id': user_id
            }
        }
