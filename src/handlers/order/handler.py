"""Get Order
"""
from random import randrange
from src.services.order.order_service import OrderService

ORDER_SERVICE = OrderService()

# pylint: disable=unused-argument
def get_order(event, context):
    """Get order handler
    """
    # for demonstration purposes always return
    # success with success with static fetch order response
    return {
        'statusCode': 200,
        'body': ORDER_SERVICE.fetch_order(order_id=randrange(1, 100))
    }
