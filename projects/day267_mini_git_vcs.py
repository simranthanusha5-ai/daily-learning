"""Day 267: Mini Git VCS."""
import hashlib

class GitObjectStore:
    def __init__(self):
        self.objects = {}

    def write_blob(self, data: bytes):
        header = f"blob {len(data)}\x00".encode()
        store_data = header + data
        sha = hashlib.sha1(store_data).hexdigest()
        self.objects[sha] = store_data
        return sha

    def write_tree(self, entries):
        # entries: [(mode, name, sha), ...]
        content = b""
        for mode, name, sha in sorted(entries, key=lambda x: x[1]):
            content += f"{mode} {name}\x00".encode() + bytes.fromhex(sha)
        header = f"tree {len(content)}\x00".encode()
        store_data = header + content
        sha = hashlib.sha1(store_data).hexdigest()
        self.objects[sha] = store_data
        return sha

    def write_commit(self, tree_sha, parent_sha, message):
        body = f"tree {tree_sha}\n"
        if parent_sha:
            body += f"parent {parent_sha}\n"
        body += f"\n{message}\n"
        content = body.encode()
        header = f"commit {len(content)}\x00".encode()
        sha = hashlib.sha1(header + content).hexdigest()
        self.objects[sha] = header + content
        return sha

if __name__ == "__main__":
    store = GitObjectStore()
    b_sha = store.write_blob(b"hello world")
    t_sha = store.write_tree([("100644", "hello.txt", b_sha)])
    c_sha = store.write_commit(t_sha, None, "Initial commit")
    assert c_sha in store.objects
    print("Day 267 Mini Git tests passed!")
