"""Day 172: Naive Bayes Text Classifier."""
import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.class_counts = defaultdict(int)
        self.word_counts = defaultdict(lambda: defaultdict(int))
        self.vocab = set()

    def train(self, docs, labels):
        for doc, label in zip(docs, labels):
            self.class_counts[label] += 1
            words = doc.lower().split()
            for w in words:
                self.vocab.add(w)
                self.word_counts[label][w] += 1

    def predict(self, doc):
        words = doc.lower().split()
        best_label, best_score = None, float('-inf')
        total_docs = sum(self.class_counts.values())

        for label, count in self.class_counts.items():
            log_prob = math.log(count / total_docs)
            total_words_label = sum(self.word_counts[label].values())
            for w in words:
                w_count = self.word_counts[label][w]
                # Laplace smoothing
                prob = (w_count + 1) / (total_words_label + len(self.vocab) + 1)
                log_prob += math.log(prob)
            if log_prob > best_score:
                best_score = log_prob
                best_label = label
        return best_label

if __name__ == "__main__":
    docs = ["great positive awesome", "terrible bad awful", "great good love", "worst horrible bad"]
    labels = ["pos", "neg", "pos", "neg"]
    nb = NaiveBayesClassifier()
    nb.train(docs, labels)
    assert nb.predict("great love") == "pos"
    assert nb.predict("terrible worst") == "neg"
    print("Day 172 Naive Bayes tests passed!")
