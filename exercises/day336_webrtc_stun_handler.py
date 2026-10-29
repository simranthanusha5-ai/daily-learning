"""Day 336: STUN Binding Request Handler."""
import struct

MAGIC_COOKIE = 0x2112A442

def create_stun_binding_response(tx_id: bytes, client_ip: str, client_port: int) -> bytes:
    msg_type = 0x0101 # Binding Success Response
    ip_parts = [int(p) for p in client_ip.split(".")]
    ip_num = (ip_parts[0] << 24) | (ip_parts[1] << 16) | (ip_parts[2] << 8) | ip_parts[3]
    x_port = client_port ^ (MAGIC_COOKIE >> 16)
    x_ip = ip_num ^ MAGIC_COOKIE
    attr = struct.pack("!HHBBH I", 0x0020, 8, 0, 1, x_port, x_ip)
    header = struct.pack("!HHI", msg_type, len(attr), MAGIC_COOKIE) + tx_id
    return header + attr

if __name__ == "__main__":
    tx = b"0123456789ab"
    resp = create_stun_binding_response(tx, "192.0.2.1", 32853)
    assert resp.startswith(b"\x01\x01")
    print("Day 336 STUN tests passed!")
