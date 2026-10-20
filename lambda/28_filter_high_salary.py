employees = [{'name': 'Yash', 'salary': 45000}, {'name': 'Dev', 'salary': 62000}, {'name': 'Manav', 'salary': 51000}]
result = list(filter(lambda employee: employee['salary'] > 50000, employees))
print(result)
