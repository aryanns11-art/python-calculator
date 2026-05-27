import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("340x500")
root.config(bg="white")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Arial", 28, "bold"),
    bd=2,
    relief=tk.FLAT,
    bg="white",
    fg="#333333",
    justify=tk.RIGHT
)

entry.pack(
    fill=tk.BOTH,
    padx=15,
    pady=20,
    ipady=20
)

frame = tk.Frame(root, bg="white")
frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:

    row_frame = tk.Frame(frame, bg="white")
    row_frame.pack(expand=True, fill="both")

    for btn in row:

        if btn == "=":
            action = calculate
            bg_color = "#66bb6a"

        elif btn in ['+', '-', '*', '/']:
            action = lambda x=btn: click(x)
            bg_color = "#64b5f6"

        else:
            action = lambda x=btn: click(x)
            bg_color = "#f1f3f6"

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18, "bold"),
            command=action,
            bg=bg_color,
            fg="#222222",
            bd=0,
            relief=tk.FLAT,
            activebackground="#dcdcdc",
            cursor="hand2"
        ).pack(
            side=tk.LEFT,
            expand=True,
            fill="both",
            padx=6,
            pady=6,
            ipady=18
        )

tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 16, "bold"),
    command=clear,
    bg="#ef5350",
    fg="white",
    bd=0,
    relief=tk.FLAT,
    activebackground="#e53935",
    cursor="hand2"
).pack(
    fill="both",
    padx=15,
    pady=10,
    ipady=12
)

root.mainloop()