def menu(opcao: int, controle: bool) -> bool:
    if opcao == 1:
        print("Insira um valor de 0 a 200")
        numero = int(input())
        numeroParaInt(numero)
        return controle
    elif opcao == 2:
        print("Saindo do programa")
        controle = False
        return controle
    else:
        print("Opção Invalida, voltando para o menu")
        return controle


def unidade(numeros_list: list, indice):
    if int(numeros_list[indice]) == 0:
        numeros_list[indice] = "zero"
        return numeros_list
    elif int(numeros_list[indice]) == 1:
        numeros_list[indice] = "um"
        return numeros_list
    elif int(numeros_list[indice]) == 2:
        numeros_list[indice] = "dois"
        return numeros_list
    elif int(numeros_list[indice]) == 3:
        numeros_list[indice] = "tres"
        return numeros_list
    elif int(numeros_list[indice]) == 4:
        numeros_list[indice] = "quatro"
        return numeros_list
    elif int(numeros_list[indice]) == 5:
        numeros_list[indice] = "cinco"
        return numeros_list
    elif int(numeros_list[indice]) == 6:
        numeros_list[indice] = "seis"
        return numeros_list
    elif int(numeros_list[indice]) == 7:
        numeros_list[indice] = "sete"
        return numeros_list
    elif int(numeros_list[indice]) == 8:
        numeros_list[indice] = "oito"
        return numeros_list
    elif int(numeros_list[indice]) == 9:
        numeros_list[indice] = "nove"
        return numeros_list
    else:
        pass


def dezena(numeros_list: list, indice):
    if int(numeros_list[indice]) == 0:
        numeros_list[indice] = ""
        return numeros_list
    if int(numeros_list[indice]) == 1:
        numeros_list[indice] = "dez"
        return numeros_list
    elif int(numeros_list[indice]) == 2:
        numeros_list[indice] = "vinte"
        return numeros_list
    elif int(numeros_list[indice]) == 3:
        numeros_list[indice] = "trinta"
        return numeros_list
    elif int(numeros_list[indice]) == 4:
        numeros_list[indice] = "quarenta"
        return numeros_list
    elif int(numeros_list[indice]) == 5:
        numeros_list[indice] = "cinquenta"
        return numeros_list
    elif int(numeros_list[indice]) == 6:
        numeros_list[indice] = "sessenta"
        return numeros_list
    elif int(numeros_list[indice]) == 7:
        numeros_list[indice] = "setenta"
        return numeros_list
    elif int(numeros_list[indice]) == 8:
        numeros_list[indice] = "oitenta"
        return numeros_list
    elif int(numeros_list[indice]) == 9:
        numeros_list[indice] = "noventa"
        return numeros_list
    else:
        pass


def dez(numeros_list: list, indice):
    if int(numeros_list[indice]) == 0:
        numeros_list[indice] = "dez"
        return numeros_list[indice]
    elif int(numeros_list[indice]) == 1:
        numeros_list[indice] = "onze"
        return numeros_list[indice]
    elif int(numeros_list[indice]) == 2:
        numeros_list[indice] = "doze "
        return numeros_list[indice]
    elif int(numeros_list[indice]) == 3:
        numeros_list[indice] = "treze"
        return numeros_list
    elif int(numeros_list[indice]) == 4:
        numeros_list[indice] = "quatorze"
        return numeros_list
    elif int(numeros_list[indice]) == 5:
        numeros_list[indice] = "quinze"
        return numeros_list
    elif int(numeros_list[indice]) == 6:
        numeros_list[indice] = "dezesseis"
        return numeros_list
    elif int(numeros_list[indice]) == 7:
        numeros_list[indice] = "dezessete"
        return numeros_list
    elif int(numeros_list[indice]) == 8:
        numeros_list[indice] = "dezoito"
        return numeros_list
    elif int(numeros_list[indice]) == 9:
        numeros_list[indice] = "dezenove"
        return numeros_list
    else:
        pass


def centena(numeros_list: list, indice):
    if int(numeros_list[indice]) == 1:
        if int(numeros_list[1]) == 0 and int(numeros_list[2]) == 0:
            numeros_list[indice] = "cem"
            return numeros_list
        else:
            numeros_list[indice] = "cento"
            return numeros_list
    elif int(numeros_list[indice]) == 2:
        numeros_list[indice] = "duzentos"
        return numeros_list
    else:
        pass


def numeroParaInt(numero: int):
    if 200 >= numero >= 0:
        numeros_list = str(numero)  # TypeCasting para str
        numeros_list = list(numeros_list)  # TypeCasting para list

        if len(numeros_list) == 1:  # Validar o tamanho da list
            resultado = unidade(numeros_list, indice=0)
            print(resultado)

        elif len(numeros_list) == 2:  # Validar o tamanho da list dezena
            if int(numeros_list[0]) == 1:  # Verificar se o numero começa com 1.
                resultado = dez(numeros_list, indice=1)  # Funcao especial para o caso dos numeros dez,onze,doze....
                if type(resultado) == list:  # Solucao para numero >= doze; por algum motivo dava erro de Type
                    resultado.pop(0)
                print(resultado)
            elif int(numeros_list[1]) == 0:  # Valida se é um numero apenas q termina em 0: 20, 10, 40...
                resultado = dezena(numeros_list, indice=0)
                print(resultado[0])
            else:
                resultado = dezena(numeros_list, indice=0)
                resultado += unidade(numeros_list, indice=1)
                print(resultado[0] + " e " + resultado[1])  # Concatenando


        elif len(numeros_list) == 3:  # Validar o tamanho da list centena
            resultado = centena(numeros_list, indice=0)
            if int(numeros_list[1]) == 1:  # Verificando se entra no "dez, onze..."
                resultado += dez(numeros_list, indice=2)
                resultado.remove('1')
                print(resultado[0] + " e " + resultado[1])
            elif int(numeros_list[1]) == 0 and int(
                    numeros_list[2]) == 0:  # Valida se é um numero "redondo" tipo 200,100...
                print(resultado[0])
            elif int(numeros_list[2]) == 0:  # Valida se é um numero apenas q termina em 0: 120, 110, 140...
                resultado = dezena(numeros_list, indice=1)
                print(resultado[0] + " e " + resultado[1])
            else:
                resultado += dezena(numeros_list, indice=1)
                resultado += unidade(numeros_list, indice=2)
                print(resultado[0] + " e " + resultado[1] + " e " + resultado[2])

    else:
        print("Numero maior que 200 ou negativo, voltando para o menu")
        return None


controle: bool = True
# print(int('3') == 3) #Teste de comparacao p/ validar o retorno
while controle:
    print("""
    1- para entrar no programa
    2- para sair da execução
    """)
    opcao = int(input())
    controle = menu(opcao, controle)
