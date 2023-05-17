from unidecode import unidecode
from unicodedata import normalize

x = "indo para o mar r ó c os"
print(x)
y = normalize('NFKD', x)
z = y.encode('ASCII', 'ignore')
print(z)

name = input("name?")

# match só da pra usar a partir do Python 3.10
match name:
    case "Harry":
        print("Gryffindor")
    case _:
        print("Default")
