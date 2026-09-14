# Day 95 Project: Bank Account Simulation
from datetime import datetime, timezone

class Account:
    def __init__(self, account_id: str, owner: str, initial_balance: float = 0.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = initial_balance
        self.ledger = []
        self._record("OPEN", initial_balance)

    def _record(self, action: str, amount: float):
        self.ledger.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "amount": amount,
            "balance_after": self.balance
        })

    def deposit(self, amount: float):
        self.balance += amount
        self._record("DEPOSIT", amount)

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record("WITHDRAWAL", amount)

acc = Account("ACC-101", "Thanusha Simran", 500.0)
acc.deposit(200.0)
acc.withdraw(150.0)
print(f"Final Balance: ${acc.balance:.2f} | Transactions: {len(acc.ledger)}")
