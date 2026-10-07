"""Day 150: Non-blocking TCP Chat Server architecture."""
import select
import socket

class MiniChatServer:
    def __init__(self, host="127.0.0.1", port=0):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.bind((host, port))
        self.server_sock.listen(5)
        self.server_sock.setblocking(False)
        self.clients = []

    def close(self):
        for client in self.clients:
            client.close()
        self.server_sock.close()

if __name__ == "__main__":
    server = MiniChatServer()
    assert server.server_sock.getsockname()[1] > 0
    server.close()
    print("Day 150 Socket Server tests passed!")
