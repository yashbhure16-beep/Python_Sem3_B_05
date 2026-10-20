"""Program 2.12: sort and filter student records."""
students = [('Yash', 82), ('Dev', 55), ('Manav', 91), ('Raj', 67), ('Vatsal', 48)]
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
passed_students = list(filter(lambda student: student[1] >= 60, students))
print('Sorted by marks:', sorted_students)
print('Marks >= 60:', passed_students)
