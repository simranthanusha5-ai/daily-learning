"""Day 160: Chain of Responsibility Middleware."""

class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return True

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("auth"):
            return False
        return super().handle(request)

class RateLimitHandler(Handler):
    def handle(self, request):
        if request.get("rate_limited"):
            return False
        return super().handle(request)

if __name__ == "__main__":
    chain = AuthHandler(RateLimitHandler())
    assert chain.handle({"auth": True, "rate_limited": False}) is True
    assert chain.handle({"auth": False}) is False
    print("Day 160 Chain of Responsibility tests passed!")
