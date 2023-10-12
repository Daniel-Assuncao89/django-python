print('Begin', __name__)

print('Define FA')


def fA():
    print('Dentro fA')

# Somente se este arquivo for o "entry point" que este bloco de codigo será executado.
# Testa se é entry point ou biblioteca.


if __name__ == '__main__':
    print('Chama fA')
    fA()

print('End', __name__)