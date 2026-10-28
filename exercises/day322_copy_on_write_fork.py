"""Day 322: Copy-on-Write Fork."""

class PhysicalFrame:
    def __init__(self, data):
        self.data = bytearray(data)
        self.ref_count = 1

class CoWAddressSpace:
    def __init__(self):
        self.pages = {} # vpage -> PhysicalFrame

    def fork(self):
        child = CoWAddressSpace()
        for vpage, frame in self.pages.items():
            frame.ref_count += 1
            child.pages[vpage] = frame
        return child

    def write(self, vpage, offset, byte_val):
        frame = self.pages[vpage]
        if frame.ref_count > 1:
            # CoW Fault: clone frame
            frame.ref_count -= 1
            new_frame = PhysicalFrame(frame.data)
            self.pages[vpage] = new_frame
            frame = new_frame
        frame.data[offset] = byte_val

if __name__ == "__main__":
    parent = CoWAddressSpace()
    parent.pages[0] = PhysicalFrame(b"parent_data")
    child = parent.fork()
    assert parent.pages[0] is child.pages[0]
    child.write(0, 0, ord('C'))
    assert parent.pages[0] is not child.pages[0]
    assert parent.pages[0].data.startswith(b"parent")
    assert child.pages[0].data.startswith(b"Carent")
    print("Day 322 CoW Fork tests passed!")
