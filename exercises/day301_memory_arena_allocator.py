"""Day 301: Contiguous Memory Arena Allocator."""

class MemoryArena:
    def __init__(self, size_bytes=1024):
        self.buffer = bytearray(size_bytes)
        self.capacity = size_bytes
        self.offset = 0

    def allocate(self, num_bytes, align=8):
        aligned_offset = (self.offset + (align - 1)) & ~(align - 1)
        if aligned_offset + num_bytes > self.capacity:
            raise MemoryError("Arena out of memory")
        ptr = aligned_offset
        self.offset = aligned_offset + num_bytes
        return ptr

    def reset(self):
        self.offset = 0

if __name__ == "__main__":
    arena = MemoryArena(256)
    p1 = arena.allocate(13, align=8)
    assert p1 == 0
    p2 = arena.allocate(10, align=8)
    assert p2 == 16 # Aligned to next multiple of 8
    arena.reset()
    assert arena.offset == 0
    print("Day 301 Memory Arena tests passed!")
