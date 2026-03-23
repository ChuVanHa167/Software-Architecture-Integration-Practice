# vấn đề: Tạo một lớp Order để đại diện cho đơn hàng trong hệ thống
# ý tưởng - Tạo một lớp Order với các phương thức để thêm sản phẩm vào đơn hàng và tính tổng số tiền của đơn hàng
# kết luận: Lớp Order sẽ có một thuộc tính items để lưu trữ các sản phẩm và số lượng, 
# một phương thức add_item để thêm sản phẩm vào đơn hàng 
# và một phương thức get_total để tính tổng số tiền của đơn hàng dựa trên giá của sản phẩm và số lượng.

class Order:

    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def get_total(self):

        total = 0

        for product, qty in self.items:
            total += product.price * qty

        return total