"""Day 302: Buddy Memory Allocator."""

class BuddyAllocator:
    def __init__(self, total_size=64):
        self.total_size = total_size
        self.free_blocks = {total_size: [0]}
        self.allocated = {}

    def allocate(self, size):
        target = 1
        while target < size:
            target <<= 1
        found_size = None
        for s in sorted(self.free_blocks.keys()):
            if s >= target and self.free_blocks[s]:
                found_size = s
                break
        if found_size is None:
            return None

        addr = self.free_blocks[found_size].pop(0)
        while found_size > target:
            found_size //= 2
            buddy_addr = addr + found_size
            self.free_blocks.setdefault(found_size, []).append(buddy_addr)
        self.allocated[addr] = target
        return addr

    def free(self, addr):
        size = self.allocated.pop(addr)
        while size < self.total_size:
            buddy = addr ^ size
            if buddy in self.free_blocks.get(size, []):
                self.free_blocks[size].remove(buddy)
                addr = min(addr, buddy)
                size *= 2
            else:
                break
        self.free_blocks.setdefault(size, []).append(addr)

if __name__ == "__main__":
    ba = BuddyAllocator(64)
    a1 = ba.allocate(15) # gets 16
    assert a1 == 0
    a2 = ba.allocate(16)
    assert a2 == 16
    ba.free(a1)
    ba.free(a2)
    assert 64 in ba.free_blocks and len(ba.free_blocks[64]) == 1
    print("Day 302 Buddy Allocator tests passed!")
