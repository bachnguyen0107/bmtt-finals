# secure_keyboard.py - mouse-driven on-screen keyboard 
# Mouse clicks type into the field, so the keyboard hook never sees the input.
# Authorized lab use only.

import tkinter as tk

KEY_ROWS = ["1234567890", "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]


class SecureKeyboard:
    def __init__(self, root):
        self.root = root
        root.title("Secure On-Screen Keyboard")
        root.resizable(False, False)

        self.entry = tk.Entry(root, font=("Consolas", 18), width=32)
        self.entry.grid(row=0, column=0, columnspan=10, padx=8, pady=10)

        for r, row_keys in enumerate(KEY_ROWS, start=1):
            for c, ch in enumerate(row_keys):
                tk.Button(root, text=ch, width=4, height=2,
                          command=lambda ch=ch: self.type_char(ch)
                          ).grid(row=r, column=c, padx=2, pady=2)

        tk.Button(root, text="SPACE", width=12,
                  command=lambda: self.type_char(" ")
                  ).grid(row=5, column=0, columnspan=3, pady=8)
        tk.Button(root, text="DEL", width=6, command=self.backspace
                  ).grid(row=5, column=3, columnspan=2, pady=8)
        tk.Button(root, text="Copy", width=6, command=self.copy
                  ).grid(row=5, column=5, columnspan=2, pady=8)
        tk.Button(root, text="Clear", width=6,
                  command=lambda: self.entry.delete(0, tk.END)
                  ).grid(row=5, column=7, columnspan=3, pady=8)

    def type_char(self, ch):
        self.entry.insert(tk.END, ch)

    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.entry.get())


def main():
    root = tk.Tk()
    SecureKeyboard(root)
    root.mainloop()


if __name__ == "__main__":
    main()