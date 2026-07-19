# Day 38: Abstract Base Classes
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Processed ${amount:.2f} via Stripe API.")
        return True

class PayPalGateway(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Processed ${amount:.2f} via PayPal Express.")
        return True

gateway: PaymentGateway = StripeGateway()
gateway.process_payment(49.99)
