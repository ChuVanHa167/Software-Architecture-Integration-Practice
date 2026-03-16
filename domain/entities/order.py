class Order:

    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def get_total(self):

        total = 0

        for product, qty in self.items:
            total += product.price * qty

        return total