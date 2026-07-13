# Day 32: Encapsulation

class BankAccount:
    def __init__(self, owner: str, initial_deposit: float = 0.0):
        self.owner = owner
        self._is_active = True
        self.__balance = max(0.0, initial_deposit)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

acc = BankAccount("Thanusha", 250.0)
acc.deposit(100.0)
print(f"{acc.owner}'s balance: ${acc.get_balance():.2f}")
