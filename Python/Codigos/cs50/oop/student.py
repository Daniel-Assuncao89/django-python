class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    # @property
    # def house(self):
    #     return self._house
    #
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name
    #
    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house


def main():
    # student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")
    # if student["name"] == "padma":
    #     student["house"] = "Ravenclaw"
    # print(f"{student['name']} from {student['house']}")
    student = Student.get()
    print(student)


# def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    # return name, house  # apesar de passar 2 variaveis elas são retornadas como uma Tuple
    # return [name, house]  # Dessa forma retornamos uma list.
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # name = input("Name: ")
    # house = input("house: ")
    # return Student(name, house)


if __name__ == "__main__":
    main()
