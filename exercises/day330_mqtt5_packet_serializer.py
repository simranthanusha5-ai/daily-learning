"""Day 330: MQTT 5.0 Packet Serializer."""
import struct

def encode_mqtt_publish(topic: str, packet_id: int, payload: bytes) -> bytes:
    topic_bytes = topic.encode()
    topic_len = len(topic_bytes)
    # Fixed header: PUBLISH (type 3), QoS 1 (flags 2) -> 0x32
    var_header = struct.pack(">H", topic_len) + topic_bytes + struct.pack(">H", packet_id)
    rem_len = len(var_header) + len(payload)
    return bytes([0x32, rem_len]) + var_header + payload

def encode_mqtt_puback(packet_id: int) -> bytes:
    # Fixed header: PUBACK (type 4) -> 0x40, len 2
    return struct.pack(">BBH", 0x40, 2, packet_id)

if __name__ == "__main__":
    pkt = encode_mqtt_publish("sensor/temp", 42, b"23.5")
    assert pkt[0] == 0x32
    ack = encode_mqtt_puback(42)
    assert ack == bytes([0x40, 0x02, 0x00, 42])
    print("Day 330 MQTT 5.0 tests passed!")
