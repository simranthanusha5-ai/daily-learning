"""Day 305: User-Space Fiber Context Switch."""

class Fiber:
    def __init__(self, target, *args):
        self.gen = target(*args)
        self.completed = False

    def resume(self):
        try:
            return next(self.gen)
        except StopIteration:
            self.completed = True
            return None

def fiber_task(name, steps, log):
    for s in range(steps):
        log.append(f"{name}:{s}")
        yield

if __name__ == "__main__":
    out = []
    f1 = Fiber(fiber_task, "F1", 2, out)
    f2 = Fiber(fiber_task, "F2", 2, out)
    while not (f1.completed and f2.completed):
        if not f1.completed: f1.resume()
        if not f2.completed: f2.resume()
    assert out == ["F1:0", "F2:0", "F1:1", "F2:1"]
    print("Day 305 Fiber tests passed!")
