from functools import reduce
from random import choice


def magic_square(line1, line2, line3):
    sum_line1 = reduce(lambda x, y: x + y, line1)
    sum_line2 = reduce(lambda x, y: x + y, line2)
    sum_line3 = reduce(lambda x, y: x + y, line3)
    sum_column1 = line1[0] + line2[0] + line3[0]
    sum_column2 = line1[1] + line2[1] + line3[1]
    sum_column3 = line1[2] + line2[2] + line3[2]
    if sum_line1 == sum_line2 == sum_line3:
        print([x for x in line1])
        print([x for x in line2])
        print([x for x in line3])
    else:
        sort_numbers()


# def repeat_numbers(matriz, numbers):
#     for num in matriz:
#         print(num, matriz[num])


def sort_numbers():
    numbers = [i for i in range(1, 11)]
    line1 = []
    # line2 = []
    # line3 = []
    matriz = []
    [matriz.append(choice(numbers)) for _ in range(1, 4) for _ in range(1, 4)]
    print(matriz)
    # [line2.append(choice(numbers)) for _ in range(1, 4)]
    # [line3.append(choice(numbers)) for _ in range(1, 4)]
    # repeat_numbers(matriz, numbers)

    # magic_square(line1, line2, line3)


sort_numbers()
