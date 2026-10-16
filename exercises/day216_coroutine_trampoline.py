"""Day 216: Coroutine Trampoline."""
from collections import deque

def task(name, n, log):
    for i in range(n):
        log.append(f"{name}:{i}")
        yield

def run_trampoline(tasks):
    queue = deque(tasks)
    while queue:
        t = queue.popleft()
        try:
            next(t)
            queue.append(t)
        except StopIteration:
            pass

if __name__ == "__main__":
    log = []
    t1 = task("A", 2, log)
    t2 = task("B", 2, log)
    run_trampoline([t1, t2])
    assert log == ["A:0", "B:0", "A:1", "B:1"]
    print("Day 216 Trampoline tests passed!")
