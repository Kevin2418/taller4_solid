class Order:


     def __init__(self, items, customer_type): 
        self.customer_type = customer_type
        self.items = [100, 50,25,15,10]



     def calculate_total(self):
         total: int = sum(self.items)


         if self.customer_type == "regular":
          total *= 0.9
         elif self.customer_type == "vip":
          total *= 0.8
         elif self.customer_type == "employee":
          total *= 0.7

         total *= 1.19
         if self.customer_type == "regular":
          total *= 0.9
         elif self.customer_type == "vip":
          total *= 0.8
         elif self.customer_type == "employee":
          total *= 0.7

         total *= 1.19

         return total