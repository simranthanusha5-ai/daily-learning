"""Day 337: Slotted Page Storage."""

class SlottedPage:
    def __init__(self, page_size=512):
        self.page_size = page_size
        self.buffer = bytearray(page_size)
        self.slots = [] # (offset, length)
        self.free_space_pointer = page_size

    def insert(self, record: bytes):
        if self.free_space_pointer - len(record) < (len(self.slots) + 1) * 4:
            return None # Out of space
        self.free_space_pointer -= len(record)
        self.buffer[self.free_space_pointer:self.free_space_pointer + len(record)] = record
        slot_id = len(self.slots)
        self.slots.append((self.free_space_pointer, len(record)))
        return slot_id

    def get(self, slot_id):
        offset, length = self.slots[slot_id]
        return bytes(self.buffer[offset:offset + length])

if __name__ == "__main__":
    page = SlottedPage(256)
    s0 = page.insert(b"row_data_alpha")
    s1 = page.insert(b"row_data_beta")
    assert page.get(s0) == b"row_data_alpha"
    assert page.get(s1) == b"row_data_beta"
    print("Day 337 Slotted Page tests passed!")
