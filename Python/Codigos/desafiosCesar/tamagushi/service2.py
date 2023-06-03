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


def menu_tamagushi(tamagushis, id):
    opcao = 2
    while opcao != 3:
        opcao = int(input("""
** PARA SAIR DIGITE QUALQUER NUMERO FORA DAS OPÇÕES **
1 - para criar novo pet
2 - listar seus pets
3 - selecionar pet
4 - deletar pet
"""))
        match opcao:
            case 1:
                tamagushis, id = add_tamagushi(tamagushis, id)
            case 2:
                list_tamagushis(tamagushis)
            case 3:
                key = int(input("Qual pet deseja?"))
                t = get_tamagushi(tamagushis, key)
                return t
            case 4:
                list_tamagushis(tamagushis)
                key = int(input("Qual pet deseja excluir?"))
                tamagushis = delete_tamagushis(tamagushis, key)
            case _:
                exit()


def create_tamagushi():
    tamagushis_dict = {}
    id = 1
    nome = input("Insira o nome para seu novo pet.").lower()
    t = Tamagushi(nome)
    tamagushis_dict[id] = t
    return tamagushis_dict, id


def add_tamagushi(tamagushis, id):
    nome = input("Insira o nome para seu novo pet.").lower()
    key = [tamagushis.get(key) for key, elemt in tamagushis.items() if nome in elemt.nome]
    if not key:
        id += 1
        t = Tamagushi(nome)
        tamagushis[id] = t
        return tamagushis, id
    print("Bixinho já existe")
    for e in key:
        tamagushis[id] = e
    return tamagushis, id


def get_tamagushi(tamagushis, key):
    t = tamagushis.get(key)
    return t


def list_tamagushis(tamagushis):
    [print(elemnt, "-", tamagushis[elemnt]) for elemnt in tamagushis.keys()]


def delete_tamagushis(tamagushis, key):
    t = tamagushis.pop(key, "Tamagushi não encontrado")
    if t:
        print("Deletado: ", t.nome)
    return tamagushis
# add_tamagushi(**tamagushi) unpacking so funciona se as keywords forem string
