# vấn đề: Tạo một use case để xử lý thanh toán đơn hàng
# ý tưởng - Tạo một lớp CheckoutOrderUseCase để xử lý thanh toán đơn hàng
# kết luận: Lớp CheckoutOrderUseCase sẽ nhận một đối tượng payment_gateway để xử lý thanh toán 
# và có một phương thức execute để thực hiện thanh toán cho đơn hàng. Phương thức này sẽ lấy tổng số tiền từ đơn hàng, 
# gọi phương thức pay của payment_gateway để thực hiện thanh toán và in ra thông báo "Order completed" khi thanh toán thành công.

class CheckoutOrderUseCase: 

    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def execute(self, order):

        total = order.get_total()

        self.payment_gateway.pay(total)

        print("Order completed")