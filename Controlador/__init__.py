from model.order_model import OrderModel # pyright: ignore[reportMissingImports]
import view.order_view # pyright: ignore[reportMissingImports]


class OrderController:

    def __init__(self, customer_type, items, payment_method):

        self.model = OrderModel(customer_type, items)
        self.view = view.order_view.OrderView()
        self.payment_method = payment_method


    def process_order(self, order_id, report_format):

        total = self.model.calculate_total()

        self.view.show_payment_message(self.payment_method)

        self.view.show_save_message(order_id)

        report = self.view.generate_report(total, report_format)

        print(report)