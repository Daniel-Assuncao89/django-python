from tamagushi import Tamagushi


def menu_tamagushi(tamagushis, id):
    opcao = 2
    while opcao != 3:
        opcao = int(input("""
1 - para criar novo pet
2 - listar seus pets
3 - selecionar pet
"""))
        match opcao:
            case 1:
                t = add_tamagushi(tamagushis, id)
                return opcao, t
            case 2:
                list_tamagushis(tamagushis)
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


def create_tamagushi():
    tamagushis_dict = {}
    id = 1
    nome = input("Insira o nome para seu novo pet.").lower()
    nome2 = "teste"
    t = Tamagushi(nome, 50, 0, 50)
    tamagushis_dict[id] = t
    return tamagushis_dict, id


def add_tamagushi(tamagushis, id):
    nome = input("Insira o nome para seu novo pet.").lower()
    key = [tamagushis.get(key) for key, elemt in tamagushis.items() if nome in elemt.nome]
    t = [Tamagushi(nome) for elemt in tamagushis.values() if nome not in elemt.nome]
    if t:
        id += 1
        for e in t:
            tamagushis[id] = e
        return tamagushis, id
    return key, id


def get_tamagushi(tamagushis, nome):
    t = [tamagushis.get(key) for key,elemt in tamagushis.items() if nome in elemt.nome]
    return t


def list_tamagushis(tamagushis):
    [print(i, "-", elemnt.nome) for i, elemnt in enumerate(tamagushis.values(), start=1)]


# add_tamagushi(**tamagushi)  unpacking so funciona se as keywords forem string

