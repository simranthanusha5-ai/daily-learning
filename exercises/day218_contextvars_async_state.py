"""Day 218: contextvars Async State."""
import contextvars
import asyncio

request_id_var = contextvars.ContextVar("request_id", default=None)

async def handle_subtask(step):
    req_id = request_id_var.get()
    return f"{req_id}:{step}"

async def handle_request(req_id):
    request_id_var.set(req_id)
    await asyncio.sleep(0.01)
    return await handle_subtask("done")

async def main():
    res1, res2 = await asyncio.gather(handle_request("req_101"), handle_request("req_202"))
    return res1, res2

if __name__ == "__main__":
    r1, r2 = asyncio.run(main())
    assert r1 == "req_101:done"
    assert r2 == "req_202:done"
    print("Day 218 ContextVars tests passed!")
