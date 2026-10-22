import tkinter as tk


def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def clear():
    display.delete(0, tk.END)


root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("300x400")

display = tk.Entry(
    root,
    font=("Arial", 20),
    justify="right"
)
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=10)


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2)
]


for text, row, column in buttons:
    tk.Button(
        root,
        text=text,
        width=6,
        height=2,
        command=lambda x=text: button_click(x)
    ).grid(row=row, column=column, padx=5, pady=5)


tk.Button(
    root,
    text="=",
    width=6,
    height=2,
    command=calculate
).grid(row=4, column=3, padx=5, pady=5)


tk.Button(
    root,
    text="Clear",
    width=25,
    height=2,
    command=clear
).grid(row=5, column=0, columnspan=4, pady=10)


root.mainloop()