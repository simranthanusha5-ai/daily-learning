"""Day 229: Compressed Bitmap Index."""

class BitmapIndex:
    def __init__(self, records, field):
        self.bitmaps = {}
        for idx, rec in enumerate(records):
            val = rec[field]
            if val not in self.bitmaps:
                self.bitmaps[val] = 0
            self.bitmaps[val] |= (1 << idx)

    def query_and(self, val1, val2):
        bm1 = self.bitmaps.get(val1, 0)
        bm2 = self.bitmaps.get(val2, 0)
        return bm1 & bm2

if __name__ == "__main__":
    records = [{"status": "ACTIVE"}, {"status": "INACTIVE"}, {"status": "ACTIVE"}]
    idx = BitmapIndex(records, "status")
    assert idx.bitmaps["ACTIVE"] == 0b101 # row 0 and 2
    print("Day 229 Bitmap Indexing tests passed!")
