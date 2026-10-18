"""Day 235: WebSocket Framing Parser."""

def parse_ws_frame(frame: bytes):
    b1, b2 = frame[0], frame[1]
    fin = (b1 >> 7) & 1
    opcode = b1 & 0x0F
    masked = (b2 >> 7) & 1
    payload_len = b2 & 0x7F

    offset = 2
    if payload_len == 126:
        offset += 2
    elif payload_len == 127:
        offset += 8

    if masked:
        mask_key = frame[offset:offset+4]
        offset += 4
        raw_payload = frame[offset:offset+payload_len]
        unmasked = bytes(b ^ mask_key[i % 4] for i, b in enumerate(raw_payload))
    else:
        unmasked = frame[offset:offset+payload_len]

    return {"fin": fin, "opcode": opcode, "payload": unmasked}

if __name__ == "__main__":
    # Ping frame unmasked with 4-byte payload
    sample = bytes([0x89, 0x04]) + b"ping"
    parsed = parse_ws_frame(sample)
    assert parsed["opcode"] == 0x09
    assert parsed["payload"] == b"ping"
    print("Day 235 WebSocket Framing tests passed!")
