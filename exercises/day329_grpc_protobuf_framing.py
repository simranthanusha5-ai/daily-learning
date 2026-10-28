"""Day 329: gRPC Message Framing."""
import struct

def frame_grpc_message(payload: bytes, compressed=False) -> bytes:
    flag = 1 if compressed else 0
    header = struct.pack(">BI", flag, len(payload))
    return header + payload

def unframe_grpc_message(data: bytes):
    flag, length = struct.unpack(">BI", data[:5])
    payload = data[5:5 + length]
    return flag == 1, payload

if __name__ == "__main__":
    msg = b"\x08\x01\x12\x04test"
    framed = frame_grpc_message(msg)
    is_comp, out = unframe_grpc_message(framed)
    assert is_comp is False
    assert out == msg
    print("Day 329 gRPC Framing tests passed!")
