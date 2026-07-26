# Day 45: contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def temporary_flag(store: dict, key: str, temp_value):
    original = store.get(key)
    store[key] = temp_value
    try:
        yield
    finally:
        if original is None:
            del store[key]
        else:
            store[key] = original

state = {"maintenance_mode": False}
print("Initial state:", state)

with temporary_flag(state, "maintenance_mode", True):
    print("Inside context:", state)

print("Restored state:", state)
