from time import sleep


from tamagushi import Tamagushi


def menu_principal(tamagushi: Tamagushi):
    opcao = 1
    while opcao != 0:
        opcao = int(input("""
1 - para alimentar
2 - para verificar o humor do pet
3 - para verificar a saude
4 - para Verificar a fome
5 - para verificar a idade
0 - para visualizar seus pets
            """))
        match opcao:
            case 1:
                tamagushi.alimentar()
            case 2:
                tamagushi.humor(tamagushi.fome, tamagushi.saude)
            case 3:
                print(f"Saude de 0 a 100: {tamagushi.saude}")
            case 4:
                print(f"Fome de 0 a 100: {tamagushi.fome}")
            case 5:
                print(f"{tamagushi.nome} tem {tamagushi.idade} ano(S)")
            case _:
                print("Indo para o menu dos pets")
    return opcao


def menu_tamagushi(tamagushis):
    opcao = 2
    while opcao != 3:
        opcao = int(input("""
1 - para criar novo pet
2 - listar seus pets
3 - selecionar pet
"""))
        match opcao:
            case 1:
                t = adicionar_tamaguchi(tamagushis)
                return opcao, t
            case 2:
                listar_tamagushis(tamagushis)
            case 3:
                indice = 1
                for elemt in tamagushis:
                    print(f"{elemt.nome} - {indice}")
                    indice += 1
                indice = int(input("Qual pet deseja?"))
                t = pegar_tamaguchi(tamagushis, indice - 1)
                return opcao, t
            case _:
                return opcao


def criar_tamagushi():
    tamagushis: list = []
    nome = input("Qual o nome que você deseja para seu novo pet?").lower()
    t = Tamagushi(nome)
    tamagushis.append(t)
    return tamagushis


def adicionar_tamaguchi(tamagushis):
    nome = input("Qual o nome que você deseja para seu novo pet?").lower()
    for elemt in tamagushis:
        if nome == elemt.nome:
            print("Este bixinho já existe, indo para o menu principal com ele")
            indice_tamagushi = tamagushis.index(elemt)
            t = pegar_tamaguchi(tamagushis, indice_tamagushi)
            return t
        else:
            t = Tamagushi(nome)
            tamagushis.append(t)
            return t


def pegar_tamaguchi(tamagushis, indice):
    t = tamagushis[indice]
    return t


def listar_tamagushis(tamagushis):
    for elemt in tamagushis:
        print(elemt.nome)
