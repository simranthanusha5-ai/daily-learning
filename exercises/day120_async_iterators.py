# Day 120: Asynchronous Iterators
import asyncio

class AsyncTicker:
    def __init__(self, limit: int):
        self.limit = limit
        self.count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.count >= self.limit:
            raise StopAsyncIteration
        await asyncio.sleep(0.01)
        self.count += 1
        return f"Tick #{self.count}"

async def main():
    async for tick in AsyncTicker(3):
        print(tick)

asyncio.run(main())
