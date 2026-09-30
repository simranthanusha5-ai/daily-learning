# Day 112: Singleton Pattern
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnectionPool(metaclass=SingletonMeta):
    def __init__(self):
        self.connection_id = "pool-primary-01"

pool1 = DatabaseConnectionPool()
pool2 = DatabaseConnectionPool()
print(f"Pool 1 ID: {pool1.connection_id}")
print(f"Is identical instance: {pool1 is pool2}")
assert pool1 is pool2
