"""Day 237: HTTP/2 HPACK Simulation."""

STATIC_TABLE = {
    1: (":authority", ""),
    2: (":method", "GET"),
    3: (":method", "POST"),
    4: (":path", "/"),
    5: (":path", "/index.html"),
    6: (":scheme", "http"),
    7: (":scheme", "https"),
    8: (":status", "200")
}

def decode_indexed_header(index: int):
    return STATIC_TABLE.get(index)

if __name__ == "__main__":
    assert decode_indexed_header(2) == (":method", "GET")
    assert decode_indexed_header(8) == (":status", "200")
    print("Day 237 HPACK tests passed!")
