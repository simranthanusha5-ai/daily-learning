"""Day 242: TLS 1.3 Handshake State Machine."""

class TLSHandshake:
    START = 0
    CLIENT_HELLO = 1
    SERVER_HELLO = 2
    ESTABLISHED = 3

    def __init__(self):
        self.state = self.START

    def send_client_hello(self):
        assert self.state == self.START
        self.state = self.CLIENT_HELLO
        return {"msg": "ClientHello", "cipher": "TLS_AES_256_GCM_SHA384"}

    def receive_server_hello(self, msg):
        assert self.state == self.CLIENT_HELLO
        if msg.get("msg") == "ServerHello":
            self.state = self.ESTABLISHED
            return True
        return False

if __name__ == "__main__":
    tls = TLSHandshake()
    ch = tls.send_client_hello()
    ok = tls.receive_server_hello({"msg": "ServerHello"})
    assert ok is True
    assert tls.state == TLSHandshake.ESTABLISHED
    print("Day 242 TLS 1.3 tests passed!")
