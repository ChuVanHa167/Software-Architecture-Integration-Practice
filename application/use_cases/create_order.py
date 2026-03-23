# vấn đề: Tạo một use case để xử lý tạo đơn hàng
# ý tưởng - Tạo một lớp CreateOrderUseCase để xử lý tạo đơn hàng
# kết luận: Lớp CreateOrderUseCase sẽ có một phương thức execute để thực hiện tạo đơn hàng.

class CreateOrderUseCase:

    def execute(self):
        from domain.entities.order import Order

        return Order()