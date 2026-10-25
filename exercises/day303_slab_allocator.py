"""Day 303: Slab Object Allocator."""

class Slab:
    def __init__(self, obj_size, num_objects):
        self.obj_size = obj_size
        self.num_objects = num_objects
        self.free_list = list(range(num_objects))

    def allocate(self):
        if not self.free_list:
            return None
        return self.free_list.pop()

    def free(self, slot_id):
        self.free_list.append(slot_id)

class SlabCache:
    def __init__(self, obj_size, slab_capacity=4):
        self.obj_size = obj_size
        self.slab_capacity = slab_capacity
        self.slabs = [Slab(obj_size, slab_capacity)]

    def get(self):
        for slab in self.slabs:
            slot = slab.allocate()
            if slot is not None:
                return (slab, slot)
        new_slab = Slab(self.obj_size, self.slab_capacity)
        self.slabs.append(new_slab)
        return (new_slab, new_slab.allocate())

if __name__ == "__main__":
    cache = SlabCache(obj_size=32, slab_capacity=2)
    s1, id1 = cache.get()
    s2, id2 = cache.get()
    s3, id3 = cache.get()
    assert len(cache.slabs) == 2
    s1.free(id1)
    assert len(s1.free_list) == 1
    print("Day 303 Slab Allocator tests passed!")
