"""Order Service
"""
from typing import Dict

class OrderService:
    """Order Service class
    """
    def __init__(self) -> None:
        """Initialize this class and assign class member(s)
        """

    def fetch_order(self, order_id: int) -> Dict:
        """Fetch order
        """
        return {
            'order': {
                'id': order_id
            }
        }

    def create_order(self, order_id: int, amount: float) -> None:
        """Create order
        """
        response: Dict = {
            'order_id': order_id,
            'amount': amount
        }
        return response
