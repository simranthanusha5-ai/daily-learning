# Day 103 Project: Directory Sync Comparator
import os

def compare_directories(source_files: dict[str, str], backup_files: dict[str, str]) -> dict:
    added = [f for f in source_files if f not in backup_files]
    deleted = [f for f in backup_files if f not in source_files]
    modified = [f for f in source_files if f in backup_files and source_files[f] != backup_files[f]]
    return {"added": added, "deleted": deleted, "modified": modified}

src = {"main.py": "hash1", "utils.py": "hash2", "config.json": "hash3"}
bak = {"main.py": "hash1", "utils.py": "hash_old", "old_temp.txt": "hash4"}

diff = compare_directories(src, bak)
print("Sync comparison diff:", diff)
