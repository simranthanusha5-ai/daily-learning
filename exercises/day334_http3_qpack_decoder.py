"""Day 334: QPACK Static Table Decoder."""

QPACK_STATIC = {
    0: (":authority", ""),
    1: (":path", "/"),
    2: (":method", "GET"),
    3: (":method", "POST"),
    4: (":scheme", "https"),
    5: (":status", "200")
}

def decode_qpack_indexed(index: int):
    return QPACK_STATIC.get(index)

if __name__ == "__main__":
    assert decode_qpack_indexed(1) == (":path", "/")
    assert decode_qpack_indexed(5) == (":status", "200")
    print("Day 334 QPACK tests passed!")
