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


def unidade(numerosList: list, indice):

        if int(numerosList[indice]) == 0:
            numerosList[indice] = "zero"
            return numerosList
        elif int(numerosList[indice]) == 1:
            numerosList[indice] = "um"
            return numerosList
        elif int(numerosList[indice]) == 2:
            numerosList[indice] = "dois"
            return numerosList
        elif int(numerosList[indice]) == 3:
            numerosList[indice] = "tres"
            return numerosList
        elif int(numerosList[indice]) == 4:
            numerosList[indice] = "quatro"
            return numerosList
        elif int(numerosList[indice]) == 5:
            numerosList[indice] = "cinco"
            return numerosList
        elif int(numerosList[indice]) == 6:
            numerosList[indice] = "seis"
            return numerosList
        elif int(numerosList[indice]) == 7:
            numerosList[indice] = "sete"
            return numerosList
        elif int(numerosList[indice]) == 8:
            numerosList[indice] = "oito"
            return numerosList
        elif int(numerosList[indice]) == 9:
            numerosList[indice] = "nove"
            return numerosList
        else:
            pass

def dezena(numerosList: list, indice):

        if int(numerosList[indice]) == 1:
            numerosList[indice] = "dez"
            return numerosList
        elif int(numerosList[indice]) == 2:
            numerosList[indice] = "vinte e "
            return numerosList
        elif int(numerosList[indice]) == 3:
            numerosList[indice] = "trinta e "
        elif int(numerosList[indice]) == 4:
            numerosList[indice] = "quarenta e"
            return numerosList
        elif int(numerosList[indice]) == 5:
            numerosList[indice] = "cinquenta e "
            return numerosList
        elif int(numerosList[indice]) == 6:
            numerosList[indice] = "sessenta e "
            return numerosList
        elif int(numerosList[indice]) == 7:
            numerosList[indice] = "setenta e "
            return numerosList
        elif int(numerosList[indice]) == 8:
            numerosList[indice] = "oitenta e "
            return numerosList
        elif int(numerosList[indice]) == 9:
            numerosList[indice] = "noventa e "
            return numerosList
        else:
            pass


def centena(numerosList: list, indice):
    if int(numerosList[indice]) == 1:
        numerosList[indice] = "cento e "
        return numerosList
    elif int(numerosList[indice]) == 2:
        numerosList[indice] = "duzentos"
        return numerosList
    else:
        pass


def numeroParaInt(numero: int):
    if (numero <= 200 and numero >= 0):
        numerosList = str(numero)  # TypeCasting para str
        # print(numerosList)
        numerosList = list(numerosList)  # TypeCasting para list
        # print(numerosList)
        # print(len(numerosList))

        if len(numerosList) == 1:
            resultado = unidade(numerosList, indice=0)
            print(resultado)

        elif len(numerosList) == 2:
            resultado = dezena(numerosList, indice=0)
            resultado += unidade(numerosList, indice=1)
            print(resultado[0:2])

        elif len(numerosList) == 3:
            resultado = centena(numerosList, indice=0)
            resultado += dezena(numerosList, indice=1)
            resultado += unidade(numerosList, indice=2)
            print(resultado[0:3])

    else:
        print("Numero maior que 200 ou negativo, voltando para o menu")
        return None


controle: bool = True
# print(int('3') == 3) #Teste de comparacao p/ validar o retorno
while controle:
    print("""
    1- para entrar no programa
    2- para sair da execucao
    """)
    opcao = int(input())
    print(opcao)
    controle = menu(opcao, controle)
