"""Day 258: W3C TraceContext Parser."""

def parse_traceparent(header: str):
    parts = header.split("-")
    if len(parts) != 4 or parts[0] != "00":
        raise ValueError("Invalid traceparent")
    return {
        "version": parts[0],
        "trace_id": parts[1],
        "parent_id": parts[2],
        "trace_flags": parts[3]
    }

def generate_child_traceparent(parent_header: str, new_span_id: str):
    parsed = parse_traceparent(parent_header)
    return f"00-{parsed['trace_id']}-{new_span_id}-{parsed['trace_flags']}"

if __name__ == "__main__":
    parent = "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"
    child = generate_child_traceparent(parent, "5a3ac9a3f9e2b4d1")
    assert "4bf92f3577b34da6a3ce929d0e0e4736" in child
    print("Day 258 Tracing tests passed!")
