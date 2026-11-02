"""Day 374: API Gateway Policy Engine."""

class APIGateway:
    def __init__(self):
        self.policies = []

    def add_policy(self, policy_fn):
        self.policies.append(policy_fn)

    def route_request(self, request):
        for policy in self.policies:
            allowed, err = policy(request)
            if not allowed:
                return {"status": 403, "error": err}
        return {"status": 200, "routed_to": f"backend_{request['path']}"}

if __name__ == "__main__":
    gw = APIGateway()
    gw.add_policy(lambda req: (req.get("role") == "admin", "Admin role required"))
    res_ok = gw.route_request({"path": "/billing", "role": "admin"})
    res_err = gw.route_request({"path": "/billing", "role": "guest"})
    assert res_ok["status"] == 200
    assert res_err["status"] == 403
    print("Day 374 API Gateway tests passed!")
