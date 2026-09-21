# Day 102 Project: Mock REST API Client

class MockHTTPResponse:
    def __init__(self, status_code: int, data: dict):
        self.status_code = status_code
        self.data = data

    @property
    def is_ok(self) -> bool:
        return 200 <= self.status_code < 300

    def json(self) -> dict:
        return self.data

def fetch_user_profile(user_id: int) -> MockHTTPResponse:
    if user_id == 1:
        return MockHTTPResponse(200, {"id": 1, "username": "simranthanusha5-ai", "active": True})
    return MockHTTPResponse(404, {"error": "User not found"})

resp = fetch_user_profile(1)
print(f"Status: {resp.status_code}, Payload: {resp.json()}")
