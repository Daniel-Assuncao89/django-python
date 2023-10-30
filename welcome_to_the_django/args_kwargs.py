# usar args é convenção, poderia ser qualquer outro nome.
def a(a, b, c, *args):
    print(a, b, c, args)  # args gera Tupla


def b(a, b, c='cD', **kwargs):  # valor padrão, caso c não tenha parametro
    print(a, b, c, kwargs)  # kwargs geram dicionario


def c(a, b, c='cD', *args, x, y, **kwargs):
    print(a, b, c, x, y, args, kwargs)


def e(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    a('A', 'B', 'C', 'D', 'E', 'F')
    b('I', 'U', z='O', k='L', r='T')
    c('A', 'B', 'C', 'D', 'E', 'F', x=1, y=2, z='O', k='L', r='T')

    t = 'A', 'B', 'C'
    d = dict(z='Z', w='W')
    e(*t, **d)
