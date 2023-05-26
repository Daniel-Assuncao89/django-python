def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return name, house  # apesar de passar 2 variaveis elas são retornadas como uma Tuple
    return [name, house]  # Dessa forma retornamos uma list.


if __name__ == "__main__":
    main()
