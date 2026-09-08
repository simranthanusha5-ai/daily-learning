# Day 89 Project: Expense Tracker
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, monthly_budget: float):
        self.budget = monthly_budget
        self.expenses = []

    def log(self, category: str, amount: float, description: str):
        self.expenses.append({"category": category, "amount": amount, "desc": description})

    def summary(self):
        totals = defaultdict(float)
        for e in self.expenses:
            totals[e["category"]] += e["amount"]
        spent = sum(totals.values())
        return {
            "budget": self.budget,
            "total_spent": spent,
            "remaining": self.budget - spent,
            "by_category": dict(totals)
        }

tracker = ExpenseTracker(monthly_budget=1500.0)
tracker.log("Food", 45.50, "Groceries")
tracker.log("Utilities", 80.00, "Internet bill")
tracker.log("Food", 22.00, "Lunch")
print("Monthly Financial Summary:", tracker.summary())
