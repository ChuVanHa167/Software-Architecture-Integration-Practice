from infrastructure.payments.payment_gateway import PaymentGateway

class PaymentFactory:

    @staticmethod
    def create():

        return PaymentGateway()