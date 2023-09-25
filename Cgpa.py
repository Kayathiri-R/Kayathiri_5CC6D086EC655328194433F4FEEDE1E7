
def sort_students(student_list):
 
    sorted_students=sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa


students = [
    Student("Alice", "A123", 3.8),
    Student("Bob", "B456", 3.6),
    Student("Charlie", "C789",3.9),
    Student("David", "D101", 3.7)
]

sorted_students=sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")