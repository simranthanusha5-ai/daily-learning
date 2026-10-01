# Day 119: Asynchronous Context Managers
import asyncio

class AsyncDatabaseSession:
    async def __aenter__(self):
        print("Acquiring async database connection...")
        await asyncio.sleep(0.01)
        return self

    async def query(self, sql: str) -> str:
        await asyncio.sleep(0.01)
        return f"Query result for: {sql}"

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing async database connection...")
        await asyncio.sleep(0.01)
        return False

async def main():
    async with AsyncDatabaseSession() as session:
        data = await session.query("SELECT * FROM learning_streak")
        print(data)

asyncio.run(main())
