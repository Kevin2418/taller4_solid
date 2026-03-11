class OrderModel:

    def __init__(self, customer_type, items):
        self.customer_type = customer_type
        self.items = items

    def calculate_total(self):

        total = sum(self.items)

        # descuentos
        if self.customer_type == "regular":
            total *= 0.9
        elif self.customer_type == "vip":
            total *= 0.8
        elif self.customer_type == "employee":
            total *= 0.7

        # impuestos
        total *= 1.19

        return total