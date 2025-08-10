students = list(range(1,31))
for _ in range(28):
    students.pop(students.index(int(input())))
    
print(students[0])
print(students[1])