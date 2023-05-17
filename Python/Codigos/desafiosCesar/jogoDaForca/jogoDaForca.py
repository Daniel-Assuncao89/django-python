from random import choice
from unidecode import unidecode


def selecao_palavra():
    with open(file="palavras.txt", mode='r', encoding='utf-8') as palavras:   # Gerenciador de contexto.
        linha = palavras.readline()
        linha1 = linha.split(sep=",")  # Transformando em list e separando por virgula.
        return choice(linha1)  # Return sempre fora do contexto de with open


def palavra_nova():
    palavra = input("Insira a palavra: ").lower()
    if type(palavra) != str:
        print("Entrada invalida!, Somente palavras são aceitas. Saindo do jogo")
        return None
    else:
        with open(file="palavras.txt", mode='r', encoding='utf-8') as palavras:
            linha = palavras.readline()
            linha1 = linha.split(sep=",")
            if palavra in linha1:
                print("Palavra já existe na lista")
                return palavra
            else:
                palavras = open(file="palavras.txt", mode='a',
                                encoding='utf8')  # Deixa o arquivo aberto e causa Memory Leak
                palavras.write(f',{palavra}')
                palavras.close()  # Para evitar o memory leak precisa fechar  manualmente.
                return palavra


def validacao_chute(chute, palavra_secreta, palavra_revelada, palavra_tratada, tentativas, acertos):
    indice = 0
    controle_acerto = False

    for char in palavra_tratada:
        if chute == char:
            acertos += 1
            palavra_revelada[indice] = char
            if acertos == len(palavra_secreta):
                print("Parabens você acertou a palavra: " + palavra_secreta + "\nSaindo do programa")
                tentativas = 0
                return tentativas, acertos, palavra_revelada
            controle_acerto = True
        indice += 1

    if controle_acerto:
        return tentativas, acertos, palavra_revelada
    else:
        tentativas -= 1
        print("Errou")
        return tentativas, acertos, palavra_revelada


def iniciar_jogo(palavra_secreta):
    tentativas = 5
    acertos = 0
    palavra_revelada = []
    palavra_tratada = unidecode(palavra_secreta)
    for char in palavra_tratada:
        # palavra_revelada.append(" ") if _ == " " else palavra_revelada
        if char == " ":
            acertos += 1
            palavra_revelada.append(" ")
        else:
            palavra_revelada.append("_")

    print("*" * 34)
    print("*    BEM VINDO AO JOGO DA FORCA  *")
    print("*" * 34)
    while tentativas > 0:
        print("Tentativas restantes: ", tentativas)
        print("Palavra: ", palavra_revelada)
        chute = input("Chute: ").lower()
        tentativas, acertos, palavra_revelada = validacao_chute(chute, palavra_secreta, palavra_revelada,
                                                                palavra_tratada, tentativas, acertos)
    if tentativas == 0 and acertos != len(palavra_secreta):
        print("Game Over. Suas tentativas acabaram")


try:
    opcao = int(input("""
Digite 1 para usar palavra aleatória
Digite 2 para inserir uma palavra
"""))
    if opcao == 1:
        palavra_secreta = selecao_palavra()
        iniciar_jogo(palavra_secreta)
    elif opcao == 2:
        palavra_secreta = palavra_nova()
        iniciar_jogo(palavra_secreta)
    else:
        print("Saindo do jogo")
except ValueError as error:
    print("Valor invalido inserido, por favor apenas numeros entre 1 e 2")
except Exception as error:
    print("Erro:")
