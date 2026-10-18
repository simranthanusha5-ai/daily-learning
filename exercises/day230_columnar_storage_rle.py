"""Day 230: Columnar Storage with RLE."""

def rle_encode(column_data):
    if not column_data:
        return []
    encoded = []
    curr = column_data[0]
    count = 1
    for x in column_data[1:]:
        if x == curr:
            count += 1
        else:
            encoded.append((curr, count))
            curr = x
            count = 1
    encoded.append((curr, count))
    return encoded

def columnar_sum(rle_col):
    return sum(val * count for val, count in rle_col)

if __name__ == "__main__":
    col = [5, 5, 5, 2, 2, 8, 8, 8, 8]
    rle = rle_encode(col)
    assert rle == [(5, 3), (2, 2), (8, 4)]
    assert columnar_sum(rle) == sum(col)
    print("Day 230 Columnar RLE tests passed!")
