def my_gen():
    n = 1
    print('Primeiro print, n é igual a {}'.format(n))
    yield n

    n += 1
    print('Segundo print, n é igual a {}'.format(n))
    yield n

    n += 1
    print('Segundo print, n é igual a {}'.format(n))
    yield n


test = my_gen()
test.__next__()
test.__next__()
test.__next__()
