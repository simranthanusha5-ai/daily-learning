"""Day 238: STOMP Protocol Frame Parser."""

def parse_stomp_frame(raw_data: str):
    lines = raw_data.strip().split("\n")
    command = lines[0].strip()
    headers = {}
    i = 1
    while i < len(lines) and lines[i].strip():
        if ":" in lines[i]:
            k, v = lines[i].split(":", 1)
            headers[k.strip()] = v.strip()
        i += 1
    body = "\n".join(lines[i+1:]).rstrip("\x00") if i + 1 < len(lines) else ""
    return {"command": command, "headers": headers, "body": body}

if __name__ == "__main__":
    frame_str = "SEND\ndestination:/queue/test\n\nHello World\x00"
    frame = parse_stomp_frame(frame_str)
    assert frame["command"] == "SEND"
    assert frame["headers"]["destination"] == "/queue/test"
    assert frame["body"] == "Hello World"
    print("Day 238 STOMP tests passed!")
