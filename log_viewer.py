# log_viewer.py - shows what keylogger.py captured
LOG_FILE = "keylog.txt"

try:
    with open(LOG_FILE, encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("No log file yet - run keylogger.py first.")
else:
    count = sum(1 for c in data if c.isprintable() and c != " ")
    print(f"Captured {count} characters:\n")
    print(data)