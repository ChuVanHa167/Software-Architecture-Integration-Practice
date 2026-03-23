from application.use_cases.create_order import CreateOrderUseCase
from application.use_cases.checkout_order import CheckoutOrderUseCase

from patterns.factory.payment_factory import PaymentFactory

from presentation.cli.order_controller import OrderController


payment_gateway = PaymentFactory.create() # Tạo đối tượng PaymentGateway thông qua PaymentFactory

create_usecase = CreateOrderUseCase() # Tạo đối tượng CreateOrderUseCase để xử lý tạo đơn hàng

checkout_usecase = CheckoutOrderUseCase(payment_gateway) # Tạo đối tượng CheckoutOrderUseCase và truyền đối tượng PaymentGateway vào để xử lý thanh toán đơn hàng

controller = OrderController(create_usecase, checkout_usecase) # Tạo đối tượng OrderController và truyền các use case vào để xử lý logic của ứng dụng trong CLI

controller.run() # Chạy phương thức run của OrderController để thực hiện các bước tạo đơn hàng, thêm sản phẩm vào đơn hàng và thanh toán đơn hàng.