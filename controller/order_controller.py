from model.order import Order
from view.order_view import OrderView


class OrderController:

    def __init__(self, customer_type, items, payment_method):

        self.customer_type = customer_type
        self.payment_method = payment_method
        self.items = items

        # crear el objeto Order
        self.order = Order(customer_type, items)

        # vista
        self.view = OrderView()

    def process_order(self, order_id, report_format):

        total = self.order.calculate_total()

        self.view.show_order(order_id, total, report_format)