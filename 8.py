def student_statistics(*marks, **details):

    minimum = min(marks)
    maximum = max(marks)
    average = sum(marks) / len(marks)

    grade_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for mark in marks:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"

        grade_count[grade] += 1

    return minimum, maximum, average, grade_count, details


# Taking student details
name = input("Enter student name: ")

marks = list(map(int, input("Enter marks separated by spaces: ").split()))

minimum, maximum, average, grades, details = student_statistics(
    *marks, name=name
)

print("\nStudent Name:", details["name"])
print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)
print("Average Marks:", round(average, 2))

print("Grade Distribution:")
for grade, count in grades.items():
    print(grade, ":", count)