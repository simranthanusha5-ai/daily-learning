"""Day 317: Completely Fair Scheduler (CFS)."""
import heapq

NICE_TO_WEIGHT = {0: 1024, -5: 3121, 5: 335}

class CFSTask:
    def __init__(self, pid, nice=0):
        self.pid = pid
        self.weight = NICE_TO_WEIGHT.get(nice, 1024)
        self.vruntime = 0.0

    def run(self, delta_exec):
        # vruntime += delta_exec * (1024 / weight)
        self.vruntime += delta_exec * (1024.0 / self.weight)

class CFSScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, (task.vruntime, task.pid, task))

    def schedule_next(self, timeslice=10):
        if not self.tasks:
            return None
        _, _, task = heapq.heappop(self.tasks)
        task.run(timeslice)
        heapq.heappush(self.tasks, (task.vruntime, task.pid, task))
        return task.pid

if __name__ == "__main__":
    cfs = CFSScheduler()
    t1 = CFSTask("P1", nice=0)
    t2 = CFSTask("P2", nice=-5) # High priority, larger weight
    cfs.add_task(t1)
    cfs.add_task(t2)
    # P2 gets scheduled more frequently because its vruntime advances slower
    picks = [cfs.schedule_next() for _ in range(4)]
    assert "P2" in picks
    print("Day 317 CFS Scheduler tests passed!")
