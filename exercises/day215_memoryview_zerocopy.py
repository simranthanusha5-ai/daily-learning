"""Day 215: Memoryview Zero-Copy Slicing."""

def mutate_buffer_slice(raw_bytes: bytearray, start: int, end: int, val: int):
    view = memoryview(raw_bytes)
    sub = view[start:end]
    for i in range(len(sub)):
        sub[i] = val
    return raw_bytes

if __name__ == "__main__":
    data = bytearray(b"abcdefgh")
    mutate_buffer_slice(data, 2, 5, ord('X'))
    assert bytes(data) == b"abXXXfgh"
    print("Day 215 Memoryview tests passed!")
