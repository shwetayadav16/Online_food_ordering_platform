import sqlite3

conn = sqlite3.connect("data/food.db")

with open("database/schema.sql") as f:
    conn.executescript(f.read())

conn.close()

print("DB created")