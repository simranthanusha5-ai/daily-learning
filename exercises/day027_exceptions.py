# Day 27: Exception Handling

class InsufficientFundsError(Exception):
    """Raised when an account withdrawal exceeds current balance."""
    def __init__(self, balance: float, amount: float):
        super().__init__(f"Cannot withdraw ${amount:.2f}: Balance is only ${balance:.2f}")
        self.balance = balance
        self.amount = amount

def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    current = withdraw(100.0, 150.0)
except InsufficientFundsError as err:
    print(f"Caught expected error: {err}")
else:
    print("Withdrawal successful!")
finally:
    print("Transaction attempt logged.")
