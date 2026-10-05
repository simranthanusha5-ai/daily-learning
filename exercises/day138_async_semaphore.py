"""Day 138: Asyncio Semaphore Rate Limiter."""
import asyncio

async def worker(sem: asyncio.Semaphore, item_id: int, results: list):
    async with sem:
        await asyncio.sleep(0.01)
        results.append(item_id * 2)

async def main():
    sem = asyncio.Semaphore(3)
    results = []
    tasks = [worker(sem, i, results) for i in range(10)]
    await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    res = asyncio.run(main())
    assert len(res) == 10
    print("Day 138 Asyncio Semaphore tests passed!")
