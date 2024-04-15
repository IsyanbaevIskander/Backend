students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

print(students | employees)
print(students.union(employees))

print(students & employees)
print(students.intersection(employees))

print(employees - students)
print(employees.difference(students))

print(students ^ employees)
print(students.symmetric_difference(employees))