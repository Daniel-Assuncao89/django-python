def menu(opcao: int, controle: bool) -> bool:
    if ( opcao == 1 ):
        print("Insira um valor de 0 a 200")
        numero = int(input())
        numeroParaInt(numero)
        return controle
    elif ( opcao == 2 ):
        print("Saindo do programa")
        controle = False
        return controle
    else:
        print("Opção Invalida, voltando para o menu")
        return controle


def numeroParaInt(numero: int):
    for num in range(200+1):
        if(num == numero):
            print("São iguais:", numero)


controle: bool = True
print("3" == 3)
while controle:
    print("""
    1- para sair da execucao
    2- para entrar no programa
    """)
    opcao = int(input())
    print(opcao)
    controle = menu(opcao, controle)

