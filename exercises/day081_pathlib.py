# Day 81: Pathlib Module
from pathlib import Path

cwd = Path(REPO_DIR)
print("Current directory:", cwd.name)

# Resolving paths cleanly
test_file = cwd / "README.md"
print(f"README exists: {test_file.exists()}")
print(f"File suffix: {test_file.suffix}")
