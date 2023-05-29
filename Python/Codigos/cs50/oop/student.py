def main():
    student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")
    if student["name"] == "padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    # #return name, house  # apesar de passar 2 variaveis elas são retornadas como uma Tuple
    # return [name, house]  # Dessa forma retornamos uma list.
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
