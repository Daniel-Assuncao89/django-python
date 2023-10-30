row = 'Henrique', 'Niterói', 22.9, 43.1


def f(t):
    nome, cidade, lat, long = t
    print(nome, cidade, lat, long)


def a(t):
    nome, cidade = t[:2]  # Cria uma tupla
    print(nome, cidade)


def b(t):
    """
    * -> simboliza que a variavel com este simbolo armazenará
    o resto do unpacking em uma lista
    """
    nome, *_, long = t
    print(nome, long, _)


if __name__ == '__main__':
    f(row)
    a(row)
    b(row)
