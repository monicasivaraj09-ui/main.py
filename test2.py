# Student Result Management System

students = ["Arun", "Priya", "Rahul", "Divya", "Kavin"]

marks = {
    "Arun": 85,
    "Priya": 92,
    "Rahul": 76,
    "Divya": 88,
    "Kavin": 69
}

def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

def display_results():
    print("Student Results")
    print("----------------")
    for student in students:
        mark = marks[student]
        grade = calculate_grade(mark)
        print(student, ":", mark, "-", grade)

display_result()

average = sum(marks.values()) / len(mark)
print("Class Average:", average)

highest = max(mark.values())
print("Highest Mark:", highest)

lowest = min(marks.values)
print("Lowest Mark:", lowest)
