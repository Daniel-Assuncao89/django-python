def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


def main():
    hello("world")
    goodbye("world")


if __name__ == "__main__":   # __name__ é atribuido automaticamente qdo roda o programa, o nome atribuido é o nome do arquivo executado, portanto qdo importamos no arquivo say.py, o main não será executado.
    main()
