# Day 98 Project: Pomodoro Session State Machine

class PomodoroSession:
    def __init__(self, work_min=25, break_min=5):
        self.work_min = work_min
        self.break_min = break_min
        self.cycle_count = 0
        self.state = "IDLE"

    def start_work(self):
        self.state = "WORKING"
        return f"Work session started ({self.work_min} minutes). Focus!"

    def complete_work(self):
        self.cycle_count += 1
        self.state = "BREAK"
        return f"Cycle {self.cycle_count} complete! Enjoy a {self.break_min} min break."

pomo = PomodoroSession()
print(pomo.start_work())
print(pomo.complete_work())
