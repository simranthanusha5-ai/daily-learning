"""Day 250: Byte-Pair Encoding (BPE)."""
from collections import Counter

def get_stats(vocab):
    pairs = Counter()
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_vocab(pair, vocab):
    v_out = {}
    bigram = " ".join(pair)
    replacement = "".join(pair)
    for word in vocab:
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = vocab[word]
    return v_out

if __name__ == "__main__":
    vocab = {"l o w </w>": 5, "l o w e r </w>": 2, "n e w e s t </w>": 6}
    pairs = get_stats(vocab)
    best_pair = pairs.most_common(1)[0][0]
    merged = merge_vocab(best_pair, vocab)
    assert any("".join(best_pair) in k for k in merged.keys())
    print("Day 250 BPE Tokenizer tests passed!")
