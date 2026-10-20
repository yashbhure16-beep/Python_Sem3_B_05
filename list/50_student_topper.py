students = [[101, 'Yash', 82], [102, 'Dev', 91], [103, 'Manav', 76]]
students.sort(key=lambda student: student[2], reverse=True)
print('Topper:', students[0])
print('Sorted students:', students)
