# Day 78: Regex Groups and Substitution
import re

text = "Issue created on 2026-09-30 by developer."
# Convert YYYY-MM-DD to DD/MM/YYYY
converted = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", text)
print("Converted date format:", converted)
