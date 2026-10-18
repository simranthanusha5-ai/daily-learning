"""Day 236: Redis RESP Protocol."""

def encode_resp_array(items):
    out = f"*{len(items)}\r\n"
    for item in items:
        s = str(item)
        out += f"${len(s)}\r\n{s}\r\n"
    return out.encode()

def parse_resp_simple_string(data: bytes):
    assert data.startswith(b"+")
    return data[1:].split(b"\r\n")[0].decode()

if __name__ == "__main__":
    cmd = encode_resp_array(["SET", "key", "val"])
    assert b"*3\r\n$3\r\nSET\r\n" in cmd
    assert parse_resp_simple_string(b"+OK\r\n") == "OK"
    print("Day 236 Redis RESP tests passed!")
