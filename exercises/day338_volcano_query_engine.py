"""Day 338: Volcano Iterator Query Engine."""

class VolcanoOperator:
    def open(self): pass
    def next(self): pass
    def close(self): pass

class SeqScan(VolcanoOperator):
    def __init__(self, rows):
        self.rows = rows
        self.idx = 0

    def open(self): self.idx = 0
    def next(self):
        if self.idx < len(self.rows):
            r = self.rows[self.idx]
            self.idx += 1
            return r
        return None

class Filter(VolcanoOperator):
    def __init__(self, child, predicate):
        self.child = child
        self.pred = predicate

    def open(self): self.child.open()
    def next(self):
        row = self.child.next()
        while row is not None:
            if self.pred(row):
                return row
            row = self.child.next()
        return None

if __name__ == "__main__":
    data = [{"id": 1, "age": 20}, {"id": 2, "age": 35}, {"id": 3, "age": 40}]
    pipeline = Filter(SeqScan(data), lambda r: r["age"] >= 30)
    pipeline.open()
    results = []
    r = pipeline.next()
    while r:
        results.append(r)
        r = pipeline.next()
    assert len(results) == 2
    print("Day 338 Volcano Query Engine tests passed!")
