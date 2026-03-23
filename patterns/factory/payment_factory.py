# vấn đề: Tạo một factory để tạo đối tượng PaymentGateway
# ý tưởng - Tạo một lớp PaymentFactory với một phương thức create để tạo đối tượng PaymentGateway
# kết luận: Lớp PaymentFactory sẽ có một phương thức create để tạo và trả về một đối tượng PaymentGateway. 
# Điều này giúp tách rời việc tạo đối tượng PaymentGateway khỏi các lớp khác trong hệ thống,

from infrastructure.payments.payment_gateway import PaymentGateway

class PaymentFactory:

    @staticmethod
    def create():

        return PaymentGateway()