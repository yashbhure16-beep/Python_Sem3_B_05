students = [{'name': 'Yash', 'marks': 78}, {'name': 'Dev', 'marks': 92}, {'name': 'Manav', 'marks': 85}]
result = sorted(students, key=lambda student: student['marks'])
print(result)
