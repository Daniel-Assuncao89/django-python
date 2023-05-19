import random


def numeros_repetidos():
    numeros = [x for x in range(1, 11)]
    matriz = []
    while len(numeros) > 0:
        num_sorteados = sortear_numeros(numeros)
        if num_sorteados in numeros:
            matriz.append(num_sorteados)
            numeros.remove(num_sorteados)
    return matriz


def sortear_numeros(numeros):
    return random.choice(numeros)


def quadrado_magico(matriz):
    line1 = sum(matriz[0:3])
    line2 = sum(matriz[3:6])
    line3 = sum(matriz[6:9])
    column1 = matriz[0] + matriz[3] + matriz[6]
    column2 = matriz[1] + matriz[4] + matriz[7]
    column3 = matriz[2] + matriz[5] + matriz[8]
    diagonal1 = matriz[0] + matriz[4] + matriz[8]
    diagonal2 = matriz[2] + matriz[4] + matriz[6]

    if line1 == line2 == line3 == column1 == column2 == column3 == diagonal1 == diagonal2:
        print(matriz[0:3], "\n", matriz[3:6], "\n", matriz[6:9])
        return False
    else:
        return True


def main():
    bool = True
    print("Processando...")
    while bool:
        matriz = numeros_repetidos()
        bool = quadrado_magico(matriz)
    print("Concluido, quadrado magico encontrado")


main()
