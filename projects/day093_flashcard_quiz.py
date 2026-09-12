# Day 93 Project: Flashcard Quiz Engine

class FlashcardQuiz:
    def __init__(self, cards: list[tuple[str, str]]):
        self.cards = cards
        self.score = 0

    def evaluate(self, user_answers: list[str]) -> dict:
        results = []
        for (q, correct), user_ans in zip(self.cards, user_answers):
            is_correct = user_ans.strip().lower() == correct.strip().lower()
            if is_correct:
                self.score += 1
            results.append({"question": q, "expected": correct, "user": user_ans, "correct": is_correct})
        return {
            "score": self.score,
            "total": len(self.cards),
            "percentage": f"{(self.score / len(self.cards)) * 100:.1f}%",
            "details": results
        }

quiz = FlashcardQuiz([
    ("What keyword defines a function in Python?", "def"),
    ("Which data structure uses LIFO order?", "stack"),
    ("What built-in function returns sequence length?", "len"),
])

summary = quiz.evaluate(["def", "stack", "len"])
print(f"Quiz passed with score: {summary['percentage']}")
