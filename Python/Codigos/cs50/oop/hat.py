import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):  # cls referencia a classe 'interna'
        house = random.choice(cls.houses)
        print(name, "is in", house)


Hat.sort("Harry")
