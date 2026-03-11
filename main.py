
## modificacion del main.py
print("El programa está corriendo")
class OrderSystem:

    def __init__(self, customer_type, items, payment_method):
        self.customer_type = customer_type
        self.items = items
        self.payment_method = payment_method

    def calculate_total(self):

        total = sum(self.items)

        if self.customer_type == "regular":
            total *= 0.9
        elif self.customer_type == "vip":
            total *= 0.8
        elif self.customer_type == "employee":
            total *= 0.7

        total *= 1.19
        return total


    def process_payment(self):

        if self.payment_method == "card":
            print("Procesando pago con tarjeta")

        elif self.payment_method == "cash":
            print("Procesando pago en efectivo")

        elif self.payment_method == "transfer":
            print("Procesando transferencia bancaria")


    def save_order(self, order_id):
        print(f"Guardando pedido {order_id} en MySQL...")


    def generate_report(self, format_type):

        total = self.calculate_total()

        if format_type == "text":
            return f"Pedido con total {total}"

        elif format_type == "csv":
            return f"total,{total}"

        elif format_type == "json":
            return f'{{"total": {total}}}'
order = OrderSystem(
    "vip",
    [100, 50, 25],
    "card")

total = order.calculate_total()

print("Total:", total)

order.process_payment()

order.save_order(1)

print(order.generate_report("text"))   
        

"""from controller.order_controller import OrderController # type: ignore


if __name__ == "__main__":

    items = [100, 50, 25]

    controller = OrderController(
        customer_type="vip",
        items=items,
        payment_method="card"
    )

    controller.process_order(order_id=1, report_format="text")"""
