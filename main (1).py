def sort_students(students):
    sorted_students = sorted(students, key=lambda x: x['cgpa'], reverse=True)
    return sorted_students
students = [
    {'name': 'Alice', 'roll_number': 'A001', 'cgpa': 3.8},
    {'name': 'Bob', 'roll_number': 'A002', 'cgpa': 3.5},
    {'name': 'Charlie', 'roll_number': 'A003', 'cgpa': 3.9},
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(student['name'], student['roll_number'], student['cgpa'])