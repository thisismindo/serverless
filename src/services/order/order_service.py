"""Order Service
"""
class OrderService:
    def fetch_order(self, order_id):
        return {
            'order': {
                'id': order_id
            }
        }
