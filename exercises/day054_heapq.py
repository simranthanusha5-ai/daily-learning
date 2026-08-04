# Day 54: Priority Queue using heapq
import heapq

# Min-heap of tasks with priority levels (lower number = higher priority)
tasks = []
heapq.heappush(tasks, (3, "Write documentation"))
heapq.heappush(tasks, (1, "Fix critical production bug"))
heapq.heappush(tasks, (2, "Review pull request"))

print("Processing tasks by priority:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"  [Priority {priority}] {task}")
