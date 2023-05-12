def menu(opcao: int, controle: bool) -> bool:
    if (opcao == 1):
        print("Insira um valor de 0 a 200")
        numero = int(input())
        numeroParaInt(numero)
        return controle
    elif (opcao == 2):
        print("Saindo do programa")
        controle = False
        return controle
    else:
        print("Opção Invalida, voltando para o menu")
        return controle


def numeroParaInt(numero: int):
    if (numero <= 200 and numero >= 0):
        numerosList = str(numero)  # TypeCasting para str
        # print(numerosList)
        numerosList = list(numerosList)  # TypeCasting para list
        # print(numerosList)

        indice = 0
        for num in numerosList:
            print(num)
            if (int(num) == 0):
                numerosList[indice] = "zero"
            elif (int(num) == 1):
                numerosList[indice] = "um"
            elif (int(num) == 2):
                numerosList[indice] = "dois"
            elif (int(num) == 3):
                numerosList[indice] = "tres"
            elif (int(num) == 4):
                numerosList[indice] = "quatro"
            elif (int(num) == 5):
                numerosList[indice] = "cinco"
            elif (int(num) == 6):
                numerosList[indice] = "seis"
            elif (int(num) == 7):
                numerosList[indice] = "sete"
            elif (int(num) == 8):
                numerosList[indice] = "oito"
            elif (int(num) == 9):
                numerosList[indice] = "nove"
            indice += 1

        print(numerosList)
    else:
        print("Numero maior que 200 ou negativo, voltando para o menu")
        return None


controle: bool = True
# print(int('3') == 3) #Teste de comparacao p/ validar o retorno
while controle:
    print("""
    1- para sair da execucao
    2- para entrar no programa
    """)
    opcao = int(input())
    print(opcao)
    controle = menu(opcao, controle)
