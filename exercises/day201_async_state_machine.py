"""Day 201: Asyncio Event-Driven State Machine."""
import asyncio

class AsyncFSM:
    def __init__(self):
        self.state = "INIT"
        self.queue = asyncio.Queue()

    async def emit(self, event):
        await self.queue.put(event)

    async def process_one(self):
        event = await self.queue.get()
        if self.state == "INIT" and event == "START":
            self.state = "RUNNING"
        elif self.state == "RUNNING" and event == "STOP":
            self.state = "STOPPED"
        self.queue.task_done()

async def test_fsm():
    fsm = AsyncFSM()
    await fsm.emit("START")
    await fsm.process_one()
    assert fsm.state == "RUNNING"
    await fsm.emit("STOP")
    await fsm.process_one()
    assert fsm.state == "STOPPED"

if __name__ == "__main__":
    asyncio.run(test_fsm())
    print("Day 201 Async FSM tests passed!")
