#Menna Musa
import re
import tkinter as tk
from tkinter import scrolledtext
# Token patterns
TOKEN_TYPES = [
    ('keyword', r'\b(int|float|char|bool|if|else|for|while|return|string)\b'),
    ('identifier', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('comment', r'//'),
    ('operator', r'==|!=|<=|>=|=|\+|-|\*|/|%'),
    ('numeric_constant', r'\b\d+(\.\d+)?\b'),
    ('special_character', r'[{}()[\];,]'),
    ('whitespace', r'\s+'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)

def scan_code():
    code = input_text.get("1.0", tk.END)
    result_text.delete("1.0", tk.END)
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'whitespace':
            result_text.insert(tk.END, f"({kind}, '{value}')\n")

# === Tkinter UI setup ===
root = tk.Tk()
root.title("Scanner For C Language ")
root.geometry("900x400")
root.configure(bg="#cfe2f3")

title = tk.Label(root, text="Scanner For C Language", font=("Arial", 16, "bold"), bg="#cfe2f3")
title.pack(pady=10)

frame = tk.Frame(root, bg="#cfe2f3")
frame.pack()

input_text = scrolledtext.ScrolledText(frame, width=40, height=15, font=("Consolas", 12))
input_text.grid(row=0, column=0, padx=10)

result_text = scrolledtext.ScrolledText(frame, width=40, height=15, font=("Consolas", 12))
result_text.grid(row=0, column=1, padx=10)

scan_button = tk.Button(root, text="Scan Code", command=scan_code, bg="#d9534f", fg="white", font=("Arial", 12, "bold"), width=15)
scan_button.pack(pady=10)

root.mainloop()