import tkinter as tk
from tkinter import messagebox


def show_frame(frame):
    frame.tkraise()


def save_data():
    with open("dashboard_data.txt", "w") as file:
        file.write("Dashboard configuration saved successfully.\n")

    messagebox.showinfo(
        "Success",
        "Dashboard data saved successfully."
    )


root = tk.Tk()
root.title("Multi-Frame Dashboard")
root.geometry("700x450")


# Create container
container = tk.Frame(root)
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)


# Create frames
home_frame = tk.Frame(container)
student_frame = tk.Frame(container)
settings_frame = tk.Frame(container)


for frame in (home_frame, student_frame, settings_frame):
    frame.grid(row=0, column=0, sticky="nsew")


# ---------------- HOME FRAME ----------------

tk.Label(
    home_frame,
    text="Welcome to Dashboard",
    font=("Arial", 24)
).pack(pady=30)

tk.Label(
    home_frame,
    text="This is the Home Page"
).pack(pady=10)


# ---------------- STUDENT FRAME ----------------

tk.Label(
    student_frame,
    text="Student Information",
    font=("Arial", 22)
).pack(pady=20)

tk.Label(
    student_frame,
    text="Name: Student"
).pack(pady=5)

tk.Label(
    student_frame,
    text="Course: B.Tech CSE"
).pack(pady=5)

tk.Label(
    student_frame,
    text="Semester: 4"
).pack(pady=5)


# ---------------- SETTINGS FRAME ----------------

tk.Label(
    settings_frame,
    text="Settings",
    font=("Arial", 22)
).pack(pady=20)

tk.Label(
    settings_frame,
    text="Dashboard Settings"
).pack(pady=10)

tk.Button(
    settings_frame,
    text="Save Configuration",
    command=save_data
).pack(pady=10)


# ---------------- MENU BAR ----------------

menu_bar = tk.Menu(root)

home_menu = tk.Menu(menu_bar, tearoff=0)
home_menu.add_command(
    label="Home",
    command=lambda: show_frame(home_frame)
)
menu_bar.add_cascade(label="Home", menu=home_menu)


student_menu = tk.Menu(menu_bar, tearoff=0)
student_menu.add_command(
    label="Student",
    command=lambda: show_frame(student_frame)
)
menu_bar.add_cascade(label="Student", menu=student_menu)


settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(
    label="Settings",
    command=lambda: show_frame(settings_frame)
)
menu_bar.add_cascade(label="Settings", menu=settings_menu)


root.config(menu=menu_bar)


# Navigation buttons
navigation = tk.Frame(root)
navigation.pack(side="bottom", pady=10)

tk.Button(
    navigation,
    text="Home",
    command=lambda: show_frame(home_frame)
).pack(side="left", padx=5)

tk.Button(
    navigation,
    text="Student",
    command=lambda: show_frame(student_frame)
).pack(side="left", padx=5)

tk.Button(
    navigation,
    text="Settings",
    command=lambda: show_frame(settings_frame)
).pack(side="left", padx=5)


show_frame(home_frame)

root.mainloop()