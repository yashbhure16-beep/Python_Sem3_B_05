"""Program 3.9: student gradebook."""
gradebook = {'Yash': [85, 80, 90], 'Dev': [72, 78, 75], 'Manav': [95, 92, 96], 'Raj': [88, 84, 86]}
averages = {name: sum(marks) / len(marks) for name, marks in gradebook.items()}
for name, average in sorted(averages.items(), key=lambda item: item[1], reverse=True):
    print(name + ':', round(average, 2))
top_student = max(averages, key=averages.get)
print('Top student:', top_student, '(' + str(round(averages[top_student], 2)) + ')')
