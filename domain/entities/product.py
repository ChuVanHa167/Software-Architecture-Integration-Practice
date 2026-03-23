# vấn đề: Tạo một lớp Product để đại diện cho sản phẩm trong hệ thống
# ý tưởng - Tạo một lớp Product với các thuộc tính id, name và price để lưu trữ thông tin về sản phẩm
# kết luận: Lớp Product sẽ có một phương thức __init__ để khởi tạo các thuộc tính id, name và price của sản phẩm. 
# Các thuộc tính này sẽ được sử dụng để lưu trữ thông tin về sản phẩm 
# và tính toán tổng số tiền của đơn hàng khi thêm sản phẩm vào đơn hàng.

class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price