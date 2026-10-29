"""Day 335: CoAP Header Parser."""
import struct

def parse_coap_header(data: bytes):
    first, code, msg_id = struct.unpack("!BBH", data[:4])
    ver = (first >> 6) & 0x03
    t = (first >> 4) & 0x03
    tkl = first & 0x0F
    return {"version": ver, "type": t, "tkl": tkl, "code": code, "msg_id": msg_id}

if __name__ == "__main__":
    # Ver 1, Confirmable (0), TKL 0 -> 0x40, Code 0.01 (GET = 1), MsgID 0x1234
    raw = bytes([0x40, 0x01, 0x12, 0x34])
    hdr = parse_coap_header(raw)
    assert hdr["version"] == 1
    assert hdr["type"] == 0
    assert hdr["code"] == 1
    assert hdr["msg_id"] == 0x1234
    print("Day 335 CoAP tests passed!")
