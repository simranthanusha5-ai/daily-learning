"""Day 227: Size-Tiered SSTable Compaction."""

def merge_sstables(tables):
    merged = {}
    for table in tables:
        for k, v in table:
            merged[k] = v
    # Filter out tombstones
    return sorted([(k, v) for k, v in merged.items() if v is not None])

if __name__ == "__main__":
    t1 = [("a", 1), ("b", 2)]
    t2 = [("b", 3), ("c", 4)]
    t3 = [("a", None)] # tombstone
    res = merge_sstables([t1, t2, t3])
    assert res == [("b", 3), ("c", 4)]
    print("Day 227 Compaction tests passed!")
