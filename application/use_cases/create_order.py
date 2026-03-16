class CreateOrderUseCase:

    def execute(self):
        from domain.entities.order import Order

        return Order()