"""Day 158: Order Processing State Machine."""

class OrderState:
    def proceed(self, order): pass

class PendingState(OrderState):
    def proceed(self, order):
        order.state = PaidState()

class PaidState(OrderState):
    def proceed(self, order):
        order.state = ShippedState()

class ShippedState(OrderState):
    def proceed(self, order):
        pass

class Order:
    def __init__(self):
        self.state = PendingState()

    def next(self):
        self.state.proceed(self)

if __name__ == "__main__":
    order = Order()
    assert isinstance(order.state, PendingState)
    order.next()
    assert isinstance(order.state, PaidState)
    order.next()
    assert isinstance(order.state, ShippedState)
    print("Day 158 State Pattern tests passed!")
