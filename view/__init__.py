class OrderView:

    def show_order(self, order_id, total, report_format):

        if report_format == "text":
            print(f"Order ID: {order_id}")
            print(f"Total: {total}")

        elif report_format == "json":
            print({
                "order_id": order_id,
                "total": total
            })