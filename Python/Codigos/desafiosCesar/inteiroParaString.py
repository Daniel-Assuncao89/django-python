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
    if int(numerosList[indice]) == 0:
        numerosList[indice] = ""
        return numerosList
    if int(numerosList[indice]) == 1:
        numerosList[indice] = "dez"
        return numerosList
    elif int(numerosList[indice]) == 2:
        numerosList[indice] = "vinte"
        return numerosList
    elif int(numerosList[indice]) == 3:
        numerosList[indice] = "trinta"
        return numerosList
    elif int(numerosList[indice]) == 4:
        numerosList[indice] = "quarenta"
        return numerosList
    elif int(numerosList[indice]) == 5:
        numerosList[indice] = "cinquenta"
        return numerosList
    elif int(numerosList[indice]) == 6:
        numerosList[indice] = "sessenta"
        return numerosList
    elif int(numerosList[indice]) == 7:
        numerosList[indice] = "setenta"
        return numerosList
    elif int(numerosList[indice]) == 8:
        numerosList[indice] = "oitenta"
        return numerosList
    elif int(numerosList[indice]) == 9:
        numerosList[indice] = "noventa"
        return numerosList
    else:
        pass


def dez(numerosList: list, indice):
    if int(numerosList[indice]) == 0:
        numerosList[indice] = "dez"
        return numerosList[indice]
    elif int(numerosList[indice]) == 1:
        numerosList[indice] = "onze"
        return numerosList[indice]
    elif int(numerosList[indice]) == 2:
        numerosList[indice] = "doze "
        return numerosList[indice]
    elif int(numerosList[indice]) == 3:
        numerosList[indice] = "treze"
        return numerosList
    elif int(numerosList[indice]) == 4:
        numerosList[indice] = "quatorze"
        return numerosList
    elif int(numerosList[indice]) == 5:
        numerosList[indice] = "quinze"
        return numerosList
    elif int(numerosList[indice]) == 6:
        numerosList[indice] = "dezesseis"
        return numerosList
    elif int(numerosList[indice]) == 7:
        numerosList[indice] = "dezessete"
        return numerosList
    elif int(numerosList[indice]) == 8:
        numerosList[indice] = "dezoito"
        return numerosList
    elif int(numerosList[indice]) == 9:
        numerosList[indice] = "dezenove"
        return numerosList
    else:
        pass


def centena(numerosList: list, indice):
    if int(numerosList[indice]) == 1:
        if int(numerosList[1]) == 0 and int(numerosList[2]) == 0:
            numerosList[indice] = "cem"
            return numerosList
        else:
            numerosList[indice] = "cento"
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

        if len(numerosList) == 1:  # Validar o tamanho da list
            resultado = unidade(numerosList, indice=0)
            print(resultado)

        elif len(numerosList) == 2:  # Validar o tamanho da list dezena
            if int(numerosList[0]) == 1:  # Verificar se o numero começa com 1.
                resultado = dez(numerosList, indice=1)  # Funcao especial para o caso dos numeros dez,onze,doze....
                if type(resultado) == list:  # Solucao para numero >= doze; por algum motivo dava erro de Type
                    resultado.pop(0)
                print(resultado)
            elif int(numerosList[1]) == 0:
                resultado = dezena(numerosList, indice=0)
                print(resultado[0])
            else:
                resultado = dezena(numerosList, indice=0)
                resultado += unidade(numerosList, indice=1)
                print(resultado[0] + " e " + resultado[1])  # Concatenando


        elif len(numerosList) == 3:   # Validar o tamanho da list centena
            resultado = centena(numerosList, indice=0)
            if int(numerosList[1]) == 1:  # Verificando se entra no "dez, onze..."
                resultado += dez(numerosList, indice=2)
                resultado.remove('1')
                print(resultado[0] + " e " + resultado[1])
            elif int(numerosList[1]) == 0 and int(numerosList[2]) == 0:
                print(resultado[0])
            elif int(numerosList[2]) == 0:
                resultado = dezena(numerosList, indice=1)
                print(resultado[0] + " e " + resultado[1])
            else:
                resultado += dezena(numerosList, indice=1)
                resultado += unidade(numerosList, indice=2)
                print(resultado[0] + " e " + resultado[1] + " e " + resultado[2])

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
