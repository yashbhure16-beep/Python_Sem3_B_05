students = [('Yash', 78), ('Dev', 92), ('Manav', 85), ('Raj', 95)]
result = sorted(students, key=lambda student: student[1], reverse=True)[:3]
print(result)
