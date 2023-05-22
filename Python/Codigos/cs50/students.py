# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")  # Atribui de forma respectiva, o valor antes da virgula a variavel name e o valor depois da virgula a variavel house
#         print(f"{name} is in {house}")
#
students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
    print(student)
