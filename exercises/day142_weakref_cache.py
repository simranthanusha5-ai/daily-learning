"""Day 142: Weak References and Caching."""
import weakref

class HeavyObject:
    def __init__(self, name):
        self.name = name

class ObjectPool:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_or_create(self, name):
        if name in self._cache:
            return self._cache[name]
        obj = HeavyObject(name)
        self._cache[name] = obj
        return obj

if __name__ == "__main__":
    pool = ObjectPool()
    obj1 = pool.get_or_create("worker_1")
    assert "worker_1" in pool._cache
    del obj1
    # Garbage collection should clear weakref
    assert "worker_1" not in pool._cache
    print("Day 142 Weakref tests passed!")
