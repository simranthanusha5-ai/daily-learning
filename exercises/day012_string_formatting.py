# Day 12: String Formatting and Manipulation

name = "Alice"
score = 98.4567
rank = 1

# Modern f-strings with precision and alignment
print(f"Player: {name:<10} | Score: {score:6.2f} | Rank: {rank:02d}")

# Multi-line template and string methods
bio = f"""
--- Profile ---
Name: {name.upper()}
Status: {'Active' if score >= 50 else 'Inactive'}
----------------
"""
print(bio.strip())

# Useful string transformation methods
sample = "  python daily learning journal  "
print("Capitalized:", sample.strip().title())
print("Replaced:", sample.replace("daily", "consistent").strip())
