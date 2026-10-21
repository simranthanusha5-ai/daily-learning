"""Day 259: CQRS Pattern."""

class WriteStore:
    def __init__(self):
        self.accounts = {}

    def handle_deposit(self, account_id, amount):
        self.accounts[account_id] = self.accounts.get(account_id, 0) + amount

class ReadProjection:
    def __init__(self):
        self.cached_balances = {}

    def sync(self, write_store):
        self.cached_balances = dict(write_store.accounts)

    def get_balance(self, account_id):
        return self.cached_balances.get(account_id, 0)

if __name__ == "__main__":
    w = WriteStore()
    r = ReadProjection()
    w.handle_deposit("acc_1", 100)
    r.sync(w)
    assert r.get_balance("acc_1") == 100
    print("Day 259 CQRS tests passed!")
