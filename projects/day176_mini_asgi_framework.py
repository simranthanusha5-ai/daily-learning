"""Day 176: Mini ASGI Web Framework."""
import json
import asyncio

class MiniASGI:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def decorator(handler):
            self.routes[path] = handler
            return handler
        return decorator

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            path = scope["path"]
            handler = self.routes.get(path)
            if handler:
                response = await handler(scope)
                status = 200
            else:
                response = {"error": "Not Found"}
                status = 404

            body = json.dumps(response).encode("utf-8")
            await send({
                "type": "http.response.start",
                "status": status,
                "headers": [[b"content-type", b"application/json"]]
            })
            await send({
                "type": "http.response.body",
                "body": body
            })

if __name__ == "__main__":
    app = MiniASGI()
    @app.route("/health")
    async def health(scope):
        return {"status": "ok"}

    assert "/health" in app.routes
    print("Day 176 Mini ASGI Framework tests passed!")
