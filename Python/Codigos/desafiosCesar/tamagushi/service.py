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
3 - para visualizar o menu principal
"""))
        match opcao:
            case 1:
                t = adicionar_tamaguchi(tamagushis)
                return opcao, t
            case 2:
                for elemnt in tamagushis:
                    print(elemnt.nome)
            case _:
                for elemt in tamagushis:
                    return opcao, elemt

def criar_tamagushi():
    tamagushis = set()
    nome = input("Qual o nome que você deseja para seu novo pet?").lower()
    t = Tamagushi(nome=nome, fome=50, idade=0, saude=50)
    tamagushis.add(t)
    return tamagushis


def adicionar_tamaguchi(tamagushis):
    nome = input("Qual o nome que você deseja para seu novo pet?").lower()
    t = Tamagushi(nome=nome, fome=50, idade=0, saude=50)
    tamagushis.add(t)
    return t
