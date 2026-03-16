class OrderController:

    def __init__(self, create_order_usecase, checkout_usecase):
        self.create_order = create_order_usecase
        self.checkout = checkout_usecase

    def run(self):

        order = self.create_order.execute()

        from domain.entities.product import Product

        product = Product(1, "Laptop", 1000)

        order.add_item(product, 1)

        self.checkout.execute(order)