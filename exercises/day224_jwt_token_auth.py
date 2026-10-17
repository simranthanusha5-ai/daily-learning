"""Day 224: JWT Token Auth."""
import json
import base64
import hashlib
import hmac

def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")

def b64url_decode(s: str) -> bytes:
    pad = '=' * (4 - len(s) % 4)
    return base64.urlsafe_b64decode(s + pad)

def encode_jwt(payload: dict, secret: str) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    h_b64 = b64url_encode(json.dumps(header).encode())
    p_b64 = b64url_encode(json.dumps(payload).encode())
    sig = hmac.new(secret.encode(), f"{h_b64}.{p_b64}".encode(), hashlib.sha256).digest()
    return f"{h_b64}.{p_b64}.{b64url_encode(sig)}"

def verify_jwt(token: str, secret: str) -> dict:
    parts = token.split(".")
    assert len(parts) == 3
    sig = hmac.new(secret.encode(), f"{parts[0]}.{parts[1]}".encode(), hashlib.sha256).digest()
    if b64url_encode(sig) != parts[2]:
        raise ValueError("Invalid signature")
    return json.loads(b64url_decode(parts[1]).decode())

if __name__ == "__main__":
    token = encode_jwt({"sub": "user_42"}, "my_secret")
    data = verify_jwt(token, "my_secret")
    assert data["sub"] == "user_42"
    print("Day 224 JWT tests passed!")
