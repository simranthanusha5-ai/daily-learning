"""Day 265: Priority Job Scheduler."""
import heapq

class PriorityScheduler:
    def __init__(self):
        self.heap = []
        self.seq = 0

    def submit(self, priority, task_name):
        heapq.heappush(self.heap, (priority, self.seq, task_name))
        self.seq += 1

    def poll(self):
        if not self.heap:
            return None
        priority, _, task_name = heapq.heappop(self.heap)
        return task_name

if __name__ == "__main__":
    ps = PriorityScheduler()
    ps.submit(priority=3, task_name="send_digest_email")
    ps.submit(priority=1, task_name="charge_credit_card")
    assert ps.poll() == "charge_credit_card"
    assert ps.poll() == "send_digest_email"
    print("Day 265 Priority Scheduler tests passed!")
