employees = [('Yash', 45000), ('Dev', 62000), ('Manav', 51000)]
result = sorted(employees, key=lambda employee: employee[1])
print(result)
