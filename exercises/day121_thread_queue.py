# Day 121: Thread-Safe Producer-Consumer Queue
import queue
import threading
import time

task_queue = queue.Queue()
results = []

def worker():
    while True:
        item = task_queue.get()
        if item is None:
            break
        # Process task
        results.append(item * 2)
        task_queue.task_done()

thread = threading.Thread(target=worker, daemon=True)
thread.start()

for num in [1, 2, 3, 4, 5]:
    task_queue.put(num)

task_queue.join()
task_queue.put(None)
thread.join()

print("Processed results from worker thread:", results)
