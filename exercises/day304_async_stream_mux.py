"""Day 304: Async Generator Stream Multiplexer."""
import asyncio

async def gen(name, count):
    for i in range(count):
        await asyncio.sleep(0.005)
        yield f"{name}:{i}"

async def mux_streams(*generators):
    queue = asyncio.Queue()
    async def worker(g):
        async for item in g:
            await queue.put(item)
        await queue.put(None)

    tasks = [asyncio.create_task(worker(g)) for g in generators]
    finished = 0
    while finished < len(generators):
        val = await queue.get()
        if val is None:
            finished += 1
        else:
            yield val
    await asyncio.gather(*tasks)

async def test_mux():
    collected = []
    async for item in mux_streams(gen("A", 2), gen("B", 2)):
        collected.append(item)
    return collected

if __name__ == "__main__":
    res = asyncio.run(test_mux())
    assert len(res) == 4
    print("Day 304 Async Stream Multiplexer tests passed!")
