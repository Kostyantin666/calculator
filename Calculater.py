import tkinter as tk
from tkinter import ttk

# === Veriables ===
current_theme = "dark"
history = []

# === Themes ===
themes = {
    "dark": {
        "bg": "#1e1e1e",
        "entry_bg": "#2e2e2e",
        "fg": "white",
        "btn_bg": "#333333",
        "top_bg": "#44475a",
        "side_bg": "#6272a4",
        "hover_bg": "#555555",
        "history_fg": "#aaaaaa",
    },
    "light": {
        "bg": "#f0f0f0",
        "entry_bg": "#ffffff",
        "fg": "black",
        "btn_bg": "#dddddd",
        "top_bg": "#e0e0e0",
        "side_bg": "#c0c0c0",
        "hover_bg": "#bbbbbb",
        "history_fg": "#666666",
    }
}

# === Functions ===
def apply_theme():
    theme = themes[current_theme]
    root.configure(bg=theme["bg"])
    display.configure(bg=theme["entry_bg"], fg=theme["fg"])
    history_label.configure(bg=theme["bg"], fg=theme["history_fg"])
    for btn in all_buttons:
        style_name = btn.original_style
        style.configure(style_name, background=theme.get(btn.bg_key, theme["btn_bg"]), foreground=theme["fg"])
        btn.configure(style=style_name)

def switch_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    theme_button.config(text="☀" if current_theme == "dark" else "🌙")
    apply_theme()

def insert_symbol(symbol):
    if symbol == "+/-":
        current = display.get()
        if current.startswith("-"):
            display.delete(0, tk.END)
            display.insert(0, current[1:])
        else:
            display.delete(0, tk.END)
            display.insert(0, "-" + current)
    elif symbol == "%":
        try:
            value = float(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(value / 100))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, symbol)

def clear_display():
    display.delete(0, tk.END)

def calculate_result():
    expr = display.get()
    try:
        result = eval(expr)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        update_history(expr + " = " + str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def update_history(entry):
    if len(history) >= 5:
        history.pop(0)
    history.append(entry)
    history_label.config(text="\n".join(history))

def on_hover(event):
    event.widget.configure(style="Hover.TButton")

def on_leave(event):
    event.widget.configure(style=event.widget.original_style)

# === Interface ===
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("360x620")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("default")
style.configure("TButton", font=("Arial", 18), padding=10, borderwidth=0, relief="flat")
style.configure("TopRow.TButton", font=("Arial", 18))
style.configure("Side.TButton", font=("Arial", 18))
style.configure("Hover.TButton", font=("Arial", 18))

# === Top: field and button of theme ===
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=(15, 0))

display = tk.Entry(top_frame, font=("Arial", 26), justify="right", borderwidth=0)
display.pack(side="left", fill="x", expand=True, ipady=15)

theme_button = ttk.Button(top_frame, text="☀", command=switch_theme, width=3)
theme_button.pack(side="right", padx=4)

# === History ===
history_label = tk.Label(root, font=("Arial", 12), anchor="w", justify="left", height=4)
history_label.pack(fill="x", padx=16, pady=(5, 5))

# === Buttons ===
button_frame = ttk.Frame(root)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ("CE", "+/-", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", ".", "=")
]

all_buttons = []

for r, row in enumerate(buttons):
    for c, label in enumerate(row):
        if label == "CE":
            command = clear_display
        elif label == "=":
            command = calculate_result
        else:
            command = lambda x=label: insert_symbol(x)

        if r == 0:
            style_name = "TopRow.TButton"
            bg_key = "top_bg"
        elif c == 3 or label == "=":
            style_name = "Side.TButton"
            bg_key = "side_bg"
        else:
            style_name = "TButton"
            bg_key = "btn_bg"

        btn = ttk.Button(button_frame, text=label, command=command, style=style_name)
        btn.original_style = style_name
        btn.bg_key = bg_key
        btn.bind("<Enter>", on_hover)
        btn.bind("<Leave>", on_leave)
        all_buttons.append(btn)

        if label == "0":
            btn.grid(row=r, column=0, columnspan=2, sticky="nsew", padx=6, pady=6)
        elif label == ".":
            btn.grid(row=r, column=2, sticky="nsew", padx=6, pady=6)
        elif label == "=":
            btn.grid(row=r, column=3, sticky="nsew", padx=6, pady=6)
        else:
            btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=6)

for i in range(len(buttons)):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

apply_theme()
root.mainloop()
