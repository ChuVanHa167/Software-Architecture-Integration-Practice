from application.use_cases.create_order import CreateOrderUseCase
from application.use_cases.checkout_order import CheckoutOrderUseCase

from patterns.factory.payment_factory import PaymentFactory

from presentation.cli.order_controller import OrderController


payment_gateway = PaymentFactory.create()

create_usecase = CreateOrderUseCase()

checkout_usecase = CheckoutOrderUseCase(payment_gateway)

controller = OrderController(create_usecase, checkout_usecase)

controller.run()