from service import *
from service2 import *


def service():
    tamagushis = criar_tamagushi()

    opcao = 1
    while 0 <= opcao <= 3:
        opcao, tamagushi = menu_tamagushi(tamagushis)
        opcao = menu_principal(tamagushi)


def service2():
    tamagushis, id = create_tamagushi()

    while True:
        menu_tamagushi(tamagushis, id)


def main():
    print("*" * 20)
    print("* ", "Bichinho Virtual", "*")
    print("*" * 20)
    service2()


if __name__ == "__main__":
    main()
