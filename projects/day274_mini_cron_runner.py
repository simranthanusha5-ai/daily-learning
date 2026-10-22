"""Day 274: Mini Cron Job Runner."""
import time

class CronJob:
    def __init__(self, interval_sec, task):
        self.interval = interval_sec
        self.task = task
        self.last_run = 0

    def check_and_run(self, current_time):
        if current_time - self.last_run >= self.interval:
            self.task()
            self.last_run = current_time
            return True
        return False

if __name__ == "__main__":
    runs = []
    job = CronJob(interval_sec=10, task=lambda: runs.append(1))
    assert job.check_and_run(100) is True
    assert job.check_and_run(105) is False
    assert job.check_and_run(111) is True
    assert len(runs) == 2
    print("Day 274 Cron Runner tests passed!")
