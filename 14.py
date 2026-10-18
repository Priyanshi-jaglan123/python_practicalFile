import pickle
import shelve


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# Create object
student = Student("Priya", 101, 85)

# Pickle serialization
with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

print("Object saved using pickle.")


# Read object using pickle
with open("student.pkl", "rb") as file:
    restored_student = pickle.load(file)

print("\nRestored object:")
restored_student.display()


# Store object using shelve
with shelve.open("student_data") as db:
    db["student1"] = student

print("\nObject saved using shelve.")


# Read object from shelve
with shelve.open("student_data") as db:
    restored = db["student1"]

print("\nObject retrieved from shelve:")
restored.display()