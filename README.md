# Software-Architecture-Integration-Practice
thực hành phần cuối trong chuỗi thực hành Software Design

# Thực Hành Software Architecture với Python

## Mini Project: Clean Architecture Order System

---

# 1. Giới thiệu

Repository này là **phần cuối cùng trong chuỗi thực hành Software Design**:

1. OOP Practice
2. SOLID Practice
3. Design Pattern Practice
4. Software Architecture Integration

Repo này kết hợp:

```
OOP
SOLID
Design Pattern
Clean Architecture
```

Mục tiêu là xây dựng **một hệ thống có kiến trúc đúng chuẩn production**.

---

# 2. Mục tiêu học tập

Sau khi hoàn thành repo này bạn sẽ:

* Biết **thiết kế hệ thống theo layer**
* Áp dụng **SOLID trong kiến trúc**
* Sử dụng **Design Pattern đúng chỗ**
* Xây dựng hệ thống **dễ mở rộng và bảo trì**

---

# 3. Kiến trúc hệ thống

Hệ thống được thiết kế theo **Clean Architecture**.

```
Presentation Layer
        ↓
Application Layer
        ↓
Domain Layer
        ↓
Infrastructure Layer
```

---

# 4. Vai trò từng layer

## Domain Layer

Chứa:

```
Entities
Business Rules
```

Ví dụ:

```
Order
Product
User
```

Domain **không phụ thuộc bất kỳ layer nào khác**.

---

## Application Layer

Chứa:

```
Use Cases
Business Flow
```

Ví dụ:

```
CreateOrderUseCase
CheckoutOrderUseCase
```

---

## Infrastructure Layer

Chứa:

```
Database
External API
Repository implementation
```

Ví dụ:

```
OrderRepository
PaymentGateway
```

---

## Presentation Layer

Chứa:

```
API
CLI
UI
```

Ở project này ta dùng **CLI đơn giản**.

---

# 5. Cấu trúc project

Tạo cấu trúc:

```
repo4-clean-architecture-order-system

src/

domain/
    entities/
        product.py
        order.py

application/
    use_cases/
        create_order.py
        checkout_order.py

infrastructure/
    repositories/
        order_repository.py

    payments/
        payment_gateway.py

presentation/
    cli/
        order_controller.py

patterns/
    factory/
        payment_factory.py

    strategy/
        discount_strategy.py

main.py
```

---

# 6. Domain Layer

File:

```
domain/entities/product.py
```

```python
class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
```

---

File:

```
domain/entities/order.py
```

```python
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
```

Domain layer **không biết database hay payment**.

---

# 7. Application Layer

File:

```
application/use_cases/create_order.py
```

```python
class CreateOrderUseCase:

    def execute(self):
        from domain.entities.order import Order

        return Order()
```

---

File:

```
application/use_cases/checkout_order.py
```

```python
class CheckoutOrderUseCase:

    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def execute(self, order):

        total = order.get_total()

        self.payment_gateway.pay(total)

        print("Order completed")
```

Ở đây áp dụng:

```
SOLID — Dependency Inversion
```

UseCase **không phụ thuộc implementation payment**.

---

# 8. Infrastructure Layer

File:

```
infrastructure/payments/payment_gateway.py
```

```python
class PaymentGateway:

    def pay(self, amount):
        print(f"Processing payment: ${amount}")
```

---

# 9. Design Pattern

## Factory Pattern

File:

```
patterns/factory/payment_factory.py
```

```python
from infrastructure.payments.payment_gateway import PaymentGateway

class PaymentFactory:

    @staticmethod
    def create():

        return PaymentGateway()
```

---

## Strategy Pattern

File:

```
patterns/strategy/discount_strategy.py
```

```python
class DiscountStrategy:

    def apply(self, price):
        return price


class TenPercentDiscount(DiscountStrategy):

    def apply(self, price):
        return price * 0.9
```

---

# 10. Presentation Layer

File:

```
presentation/cli/order_controller.py
```

```python
class OrderController:

    def __init__(self, create_order_usecase, checkout_usecase):
        self.create_order = create_order_usecase
        self.checkout = checkout_usecase

    def run(self):

        order = self.create_order.execute()

        from domain.entities.product import Product

        product = Product(1, "Laptop", 1000)

        order.add_item(product, 1)

        self.checkout.execute(order)
```

---

# 11. Main Program

File:

```
main.py
```

```python
from application.use_cases.create_order import CreateOrderUseCase
from application.use_cases.checkout_order import CheckoutOrderUseCase

from patterns.factory.payment_factory import PaymentFactory

from presentation.cli.order_controller import OrderController


payment_gateway = PaymentFactory.create()

create_usecase = CreateOrderUseCase()

checkout_usecase = CheckoutOrderUseCase(payment_gateway)

controller = OrderController(create_usecase, checkout_usecase)

controller.run()
```

---

# 12. Những gì project này áp dụng

OOP

```
Entities
Encapsulation
```

---

SOLID

```
SRP
DIP
OCP
```

---

Design Pattern

```
Factory
Strategy
```

---

Architecture

```
Clean Architecture
Layered Design
```

---

# 13. Kết quả sau khi hoàn thành

Bạn sẽ hiểu:

```
OOP
SOLID
Design Pattern
Software Architecture
```

và có thể **thiết kế hệ thống production-level**.

---

# 14. Sau chuỗi thực hành này

Bạn nên tiếp tục học:

```
Advanced Design Pattern
Domain Driven Design
Microservice Architecture
System Design
```

để tiến tới **Senior Software Engineer level**.
