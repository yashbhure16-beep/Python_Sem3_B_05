students = [('Yash', 78), ('Dev', 35), ('Manav', 85), ('Raj', 28)]
passed = filter(lambda student: student[1] >= 35, students)
result = sorted(passed, key=lambda student: student[1])
print(result)
