# vấn đề: Tạo một chiến lược giảm giá để áp dụng cho đơn hàng
# ý tưởng - Tạo một lớp DiscountStrategy với một phương thức apply để áp dụng giảm giá cho một mức giá nhất định. 
# Sau đó, tạo một lớp TenPercentDiscount kế thừa từ DiscountStrategy để áp dụng giảm giá 10% cho mức giá.
# kết luận: Lớp DiscountStrategy sẽ có một phương thức apply nhận một tham số price và trả về giá sau khi áp dụng giảm giá. 
# Lớp TenPercentDiscount sẽ ghi đè phương thức apply để trả về giá sau khi giảm 10%


class DiscountStrategy:

    def apply(self, price):
        return price


class TenPercentDiscount(DiscountStrategy):

    def apply(self, price):
        return price * 0.9
