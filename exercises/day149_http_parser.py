"""Day 149: HTTP/1.1 Request Parser."""

def parse_http_request(raw_data: bytes):
    text = raw_data.decode('utf-8', errors='replace')
    parts = text.split("

", 1)
    header_section = parts[0]
    body = parts[1] if len(parts) > 1 else ""

    lines = header_section.split("
")
    request_line = lines[0].split(" ")
    method, path, version = request_line[0], request_line[1], request_line[2]

    headers = {}
    for line in lines[1:]:
        if ": " in line:
            k, v = line.split(": ", 1)
            headers[k.lower()] = v

    return {
        "method": method,
        "path": path,
        "version": version,
        "headers": headers,
        "body": body
    }

if __name__ == "__main__":
    sample = b"GET /api/v1/users HTTP/1.1
Host: example.com
Accept: application/json

"
    parsed = parse_http_request(sample)
    assert parsed["method"] == "GET"
    assert parsed["path"] == "/api/v1/users"
    assert parsed["headers"]["host"] == "example.com"
    print("Day 149 HTTP Parser tests passed!")
