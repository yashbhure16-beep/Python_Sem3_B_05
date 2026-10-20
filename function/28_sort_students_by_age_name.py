students = [{'name': 'Yash', 'age': 25}, {'name': 'Dev', 'age': 22}, {'name': 'Manav', 'age': 25}]
result = sorted(students, key=lambda student: (student['age'], student['name']))
print(result)
