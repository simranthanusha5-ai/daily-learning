# Day 108: SQLite Database Operations
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE learning_logs (
    day INTEGER PRIMARY KEY,
    topic TEXT NOT NULL,
    date TEXT NOT NULL
);
""")

cursor.execute("INSERT INTO learning_logs VALUES (?, ?, ?)", (108, "SQLite Basics", "2026-09-30"))
conn.commit()

cursor.execute("SELECT * FROM learning_logs;")
row = cursor.fetchone()
print("Retrieved SQLite row:", row)
conn.close()
