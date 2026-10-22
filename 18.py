import tkinter as tk
from tkinter import messagebox


def save_record():
    name = name_entry.get()
    roll = roll_entry.get()
    course = course_entry.get()
    gender = gender_var.get()

    hobbies = []

    if reading_var.get():
        hobbies.append("Reading")

    if sports_var.get():
        hobbies.append("Sports")

    if music_var.get():
        hobbies.append("Music")

    address = address_text.get("1.0", tk.END).strip()

    if name == "" or roll == "" or course == "":
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    with open("student_records.txt", "a") as file:
        file.write("Name: " + name + "\n")
        file.write("Roll No: " + roll + "\n")
        file.write("Course: " + course + "\n")
        file.write("Gender: " + gender + "\n")
        file.write("Hobbies: " + ", ".join(hobbies) + "\n")
        file.write("Address: " + address + "\n")
        file.write("-" * 40 + "\n")

    messagebox.showinfo("Success", "Student record saved successfully.")


def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)

    gender_var.set("Male")
    reading_var.set(False)
    sports_var.set(False)
    music_var.set(False)


root = tk.Tk()
root.title("Student Record Manager")
root.geometry("400x500")

tk.Label(root, text="Student Record Manager",
         font=("Arial", 18)).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root, width=40)
roll_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root, width=40)
course_entry.pack()

tk.Label(root, text="Gender").pack()

gender_var = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male",
               variable=gender_var,
               value="Male").pack()

tk.Radiobutton(root, text="Female",
               variable=gender_var,
               value="Female").pack()

tk.Label(root, text="Hobbies").pack()

reading_var = tk.BooleanVar()
sports_var = tk.BooleanVar()
music_var = tk.BooleanVar()

tk.Checkbutton(root, text="Reading",
               variable=reading_var).pack()

tk.Checkbutton(root, text="Sports",
               variable=sports_var).pack()

tk.Checkbutton(root, text="Music",
               variable=music_var).pack()

tk.Label(root, text="Address").pack()

address_text = tk.Text(root, width=35, height=4)
address_text.pack()

tk.Button(root, text="Save Record",
          command=save_record).pack(pady=10)

tk.Button(root, text="Clear",
          command=clear_fields).pack()

root.mainloop()