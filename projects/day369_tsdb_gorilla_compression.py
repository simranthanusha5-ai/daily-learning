"""Day 369: Gorilla TSDB Delta-of-Delta."""

def compress_timestamps(timestamps):
    if not timestamps:
        return []
    deltas = [timestamps[0]]
    if len(timestamps) > 1:
        deltas.append(timestamps[1] - timestamps[0])
    for i in range(2, len(timestamps)):
        d_prev = timestamps[i-1] - timestamps[i-2]
        d_curr = timestamps[i] - timestamps[i-1]
        dod = d_curr - d_prev
        deltas.append(dod)
    return deltas

def decompress_timestamps(compressed):
    if not compressed:
        return []
    out = [compressed[0]]
    if len(compressed) > 1:
        prev_d = compressed[1]
        out.append(out[-1] + prev_d)
        for dod in compressed[2:]:
            curr_d = prev_d + dod
            out.append(out[-1] + curr_d)
            prev_d = curr_d
    return out

if __name__ == "__main__":
    ts = [1000, 1060, 1120, 1180, 1240]
    comp = compress_timestamps(ts)
    assert comp[2:] == [0, 0, 0] # Constant delta yields 0 dod
    assert decompress_timestamps(comp) == ts
    print("Day 369 Gorilla TSDB tests passed!")
