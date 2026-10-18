"""Day 231: Inverted Index with TF-IDF."""
import math
from collections import defaultdict

class SearchIndex:
    def __init__(self):
        self.docs = {}
        self.index = defaultdict(set)

    def add_doc(self, doc_id, text):
        words = text.lower().split()
        self.docs[doc_id] = words
        for w in words:
            self.index[w].add(doc_id)

    def search(self, query):
        words = query.lower().split()
        scores = defaultdict(float)
        num_docs = len(self.docs)

        for w in words:
            matching_docs = self.index.get(w, set())
            if not matching_docs:
                continue
            idf = math.log((num_docs + 1) / (len(matching_docs) + 1)) + 1
            for doc_id in matching_docs:
                tf = self.docs[doc_id].count(w) / len(self.docs[doc_id])
                scores[doc_id] += tf * idf
        return sorted(scores.keys(), key=lambda d: scores[d], reverse=True)

if __name__ == "__main__":
    idx = SearchIndex()
    idx.add_doc(1, "python database engine internals")
    idx.add_doc(2, "python programming web framework")
    results = idx.search("database engine")
    assert results[0] == 1
    print("Day 231 Inverted Index tests passed!")
