"""Day 339: Vectorized Batch Query Engine."""

class ColumnBatch:
    def __init__(self, cols):
        self.cols = cols # dict of name -> list of values
        self.size = len(next(iter(cols.values())))

def vectorized_filter(batch, col_name, thresh):
    col = batch.cols[col_name]
    # Bitmask selection
    selection = [i for i, val in enumerate(col) if val > thresh]
    filtered_cols = {name: [col_data[i] for i in selection] for name, col_data in batch.cols.items()}
    return ColumnBatch(filtered_cols)

if __name__ == "__main__":
    b = ColumnBatch({"id": [1, 2, 3, 4], "price": [10, 50, 20, 80]})
    out = vectorized_filter(b, "price", 25)
    assert out.cols["id"] == [2, 4]
    print("Day 339 Vectorized Query tests passed!")
