# Day 24: File I/O Operations
import tempfile
import os

with tempfile.TemporaryDirectory() as tmpdir:
    filepath = os.path.join(tmpdir, "sample.txt")
    
    # Writing lines safely
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("Line 1: Hello from Python File I/O\n")
        f.write("Line 2: Context managers auto-close handles\n")
        f.write("Line 3: Persistent learning log\n")
    
    # Reading lines
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    
    print(f"Read {len(lines)} lines:")
    for line in lines:
        print(f"  > {line}")
