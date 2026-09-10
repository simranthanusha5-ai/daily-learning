# Day 91 Project: Text Analyzer
import re

def analyze_text(text: str) -> dict:
    words = re.findall(r"\b\w+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    word_count = len(words)
    unique_words = len(set(words))
    reading_time_min = round(word_count / 200, 2)
    
    return {
        "words": word_count,
        "unique_words": unique_words,
        "sentences": len(sentences),
        "est_reading_minutes": reading_time_min,
        "lexical_diversity": round(unique_words / word_count, 2) if word_count else 0
    }

doc = "Python is an interpreted, high-level programming language. Python emphasizes readability."
print("Text Analysis:", analyze_text(doc))
