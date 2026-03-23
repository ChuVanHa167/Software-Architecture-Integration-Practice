# vấn đề: Tạo một lớp PaymentGateway để xử lý thanh toán trong hệ thống
# ý tưởng - Tạo một lớp PaymentGateway với một phương thức pay để xử lý thanh toán cho đơn hàng
# kết luận: Lớp PaymentGateway sẽ có một phương thức pay nhận một tham số amount để xử lý thanh toán. 
# Phương thức này sẽ in ra thông báo "Processing payment: $amount" để mô phỏng quá trình thanh toán.


class PaymentGateway:

    def pay(self, amount):
        print(f"Processing payment: ${amount}")