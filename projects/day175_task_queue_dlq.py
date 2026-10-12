"""Day 175: Task Queue with Dead-Letter Queue."""
from collections import deque

class TaskQueue:
    def __init__(self, max_retries=3):
        self.queue = deque()
        self.dlq = deque()
        self.max_retries = max_retries

    def push(self, task):
        self.queue.append({"data": task, "retries": 0})

    def process_all(self, handler):
        while self.queue:
            item = self.queue.popleft()
            try:
                handler(item["data"])
            except Exception as e:
                item["retries"] += 1
                if item["retries"] >= self.max_retries:
                    self.dlq.append(item)
                else:
                    self.queue.append(item)

if __name__ == "__main__":
    tq = TaskQueue(max_retries=2)
    tq.push("fail_job")
    def buggy(data): raise ValueError("err")
    tq.process_all(buggy)
    assert len(tq.dlq) == 1
    assert tq.dlq[0]["data"] == "fail_job"
    print("Day 175 Task Queue tests passed!")
