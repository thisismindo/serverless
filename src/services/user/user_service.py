"""User Service
"""
from typing import Dict

class UserService:
    """User service class
    """
    def __init__(self) -> None:
        """Initialize this class and assign class member(s)
        """

    def fetch_user(self, user_id: int) -> Dict:
        """Fetch user
        """
        return {
            'user': {
                'id': user_id
            }
        }

    def create_user(self, name: str, email: str) -> None:
        """Create user
        """
        response: Dict = {
            'name': name,
            'email': email
        }
        return response
