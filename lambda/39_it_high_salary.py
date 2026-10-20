employees = [('Yash', 'IT', 55000), ('Dev', 'HR', 62000), ('Manav', 'IT', 48000), ('Raj', 'IT', 72000)]
result = list(filter(lambda employee: employee[1] == 'IT' and employee[2] > 50000, employees))
print(result)
