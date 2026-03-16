class CheckoutOrderUseCase:

    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def execute(self, order):

        total = order.get_total()

        self.payment_gateway.pay(total)

        print("Order completed")