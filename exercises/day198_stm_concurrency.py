"""Day 198: Software Transactional Memory."""
import threading

class TVar:
    def __init__(self, val):
        self.val = val
        self.version = 0

class Transaction:
    def __init__(self):
        self.read_set = {}
        self.write_set = {}

    def read(self, tvar):
        if tvar in self.write_set:
            return self.write_set[tvar]
        self.read_set[tvar] = (tvar.val, tvar.version)
        return tvar.val

    def write(self, tvar, val):
        self.write_set[tvar] = val

_stm_lock = threading.Lock()

def atomically(tx_func, retries=5):
    for _ in range(retries):
        tx = Transaction()
        res = tx_func(tx)
        with _stm_lock:
            conflict = False
            for tvar, (_, ver) in tx.read_set.items():
                if tvar.version != ver:
                    conflict = True
                    break
            if not conflict:
                for tvar, new_val in tx.write_set.items():
                    tvar.val = new_val
                    tvar.version += 1
                return res
    raise RuntimeError("Transaction conflict limit exceeded")

if __name__ == "__main__":
    acc1 = TVar(100)
    acc2 = TVar(50)
    def transfer(tx):
        b1 = tx.read(acc1)
        b2 = tx.read(acc2)
        tx.write(acc1, b1 - 25)
        tx.write(acc2, b2 + 25)
    atomically(transfer)
    assert acc1.val == 75
    assert acc2.val == 75
    print("Day 198 STM tests passed!")
