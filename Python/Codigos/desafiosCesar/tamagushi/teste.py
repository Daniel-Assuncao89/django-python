from tamagushi import Tamagushi

nome = input("Insira o nome")
t = Tamagushi(nome=nome, fome=50, idade=0, saude=50)
tam = {1: t}
nome = input("Insira o nome")
t2 = Tamagushi(nome=nome, fome=50, idade=0, saude=50)
tam[2] = t2
pegar = int(input("nome para pegar"))
get = tam.get(pegar, "Bixinho não encontrado")
print(type(get))  # Retorna uma tupla

for elemt in tam.values():
    print(type(elemt))
    print(elemt.nome)
