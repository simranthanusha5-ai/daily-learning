"""Day 375: Distributed MapReduce Engine."""
from collections import defaultdict

def mapreduce_run(data, mapper, reducer):
    # Map phase
    intermediate = defaultdict(list)
    for item in data:
        for k, v in mapper(item):
            intermediate[k].append(v)
    # Reduce phase
    output = {}
    for k, values in intermediate.items():
        output[k] = reducer(k, values)
    return output

if __name__ == "__main__":
    docs = ["apple orange apple", "orange banana"]
    def word_count_map(doc):
        return [(w, 1) for w in doc.split()]
    def word_count_reduce(k, vals):
        return sum(vals)

    counts = mapreduce_run(docs, word_count_map, word_count_reduce)
    assert counts["apple"] == 2
    assert counts["orange"] == 2
    assert counts["banana"] == 1
    print("Day 375 MapReduce tests passed!")
