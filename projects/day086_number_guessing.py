# Day 86 Project: Number Guessing Game Engine
import random

class NumberGuessingGame:
    def __init__(self, secret: int = None, max_attempts: int = 7):
        self.secret = secret if secret is not None else random.randint(1, 100)
        self.max_attempts = max_attempts
        self.attempts = 0
        self.is_over = False

    def guess(self, number: int) -> str:
        if self.is_over:
            return "Game is already over."
        self.attempts += 1
        if number == self.secret:
            self.is_over = True
            return f"Correct! Found in {self.attempts} attempts."
        if self.attempts >= self.max_attempts:
            self.is_over = True
            return f"Game over! Secret was {self.secret}."
        return "Too high!" if number > self.secret else "Too low!"

game = NumberGuessingGame(secret=42)
print("Guess 20:", game.guess(20))
print("Guess 50:", game.guess(50))
print("Guess 42:", game.guess(42))
