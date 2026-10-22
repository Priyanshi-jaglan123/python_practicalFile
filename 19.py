import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def open_file():
    global photo

    filename = filedialog.askopenfilename(
        title="Select File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Image Files", "*.png *.jpg *.jpeg"),
            ("All Files", "*.*")
        ]
    )

    if filename == "":
        return

    try:
        if filename.lower().endswith(".txt"):
            with open(filename, "r") as file:
                content = file.read()

            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

            image_label.config(image="")
            file_label.config(text="Text File: " + filename)

        else:
            image = Image.open(filename)
            image.thumbnail((500, 350))

            photo = ImageTk.PhotoImage(image)

            image_label.config(image=photo)
            text_area.delete("1.0", tk.END)

            file_label.config(text="Image File: " + filename)

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Image / File Viewer")
root.geometry("650x550")

tk.Label(
    root,
    text="Dynamic File and Image Viewer",
    font=("Arial", 18)
).pack(pady=10)

tk.Button(
    root,
    text="Open File",
    command=open_file
).pack(pady=10)

file_label = tk.Label(root, text="No file selected")
file_label.pack()

text_area = tk.Text(root, width=70, height=15)
text_area.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

root.mainloop()