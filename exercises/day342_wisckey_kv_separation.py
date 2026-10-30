"""Day 342: WiscKey Key-Value Separation."""

class WiscKeyStore:
    def __init__(self):
        self.vlog = [] # Value Log
        self.lsm_index = {} # Key -> (vlog_offset, length)

    def put(self, key, value):
        offset = len(self.vlog)
        self.vlog.append(value)
        self.lsm_index[key] = (offset, len(value))

    def get(self, key):
        if key not in self.lsm_index:
            return None
        offset, _ = self.lsm_index[key]
        return self.vlog[offset]

if __name__ == "__main__":
    wk = WiscKeyStore()
    wk.put("img_1", b"PNG_DATA_BLOB")
    assert wk.get("img_1") == b"PNG_DATA_BLOB"
    print("Day 342 WiscKey tests passed!")
