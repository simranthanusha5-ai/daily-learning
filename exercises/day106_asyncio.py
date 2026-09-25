# Day 106: asyncio Basics
import asyncio

async def fetch_data(source: str, delay: float) -> str:
    print(f"Starting fetch from {source}...")
    await asyncio.sleep(delay)
    return f"Data from {source}"

async def main():
    results = await asyncio.gather(
        fetch_data("API Server 1", 0.05),
        fetch_data("API Server 2", 0.08),
    )
    for r in results:
        print("Received:", r)

asyncio.run(main())
