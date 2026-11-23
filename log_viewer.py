# log_viewer.py - Reads keylog.txt and summarises the captured keystrokes.


import os

LOG_FILE = "keylog.txt"


def main() -> None:
    if not os.path.exists(LOG_FILE):
        print(f"[!] {LOG_FILE} not found. Run keylogger.py first.")
        return

    with open(LOG_FILE, encoding="utf-8") as f:
        data = f.read()

    printable = sum(1 for c in data if c.isprintable() and c != " ")
    spaces = data.count(" ")
    newlines = data.count("\n")

    print("=" * 50)
    print(" KEYLOG ANALYSIS")
    print("=" * 50)
    print(f" Printable characters : {printable}")
    print(f" Spaces               : {spaces}")
    print(f" Enter / newlines     : {newlines}")
    print(f" Total characters     : {len(data)}")
    print("-" * 50)
    print(" Reconstructed input:")
    print("-" * 50)
    print(data)


if __name__ == "__main__":
    main()
