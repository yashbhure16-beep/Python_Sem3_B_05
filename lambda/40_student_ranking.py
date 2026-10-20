students = [('Yash', 78), ('Dev', 92), ('Manav', 85), ('Raj', 95)]
ranking = sorted(students, key=lambda student: student[1], reverse=True)
for position, student in enumerate(ranking, 1):
    print(position, student[0], student[1])
