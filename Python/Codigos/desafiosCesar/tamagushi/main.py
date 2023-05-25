from tamagushi import Tamagushi
from service import *

print("*" * 20)
print("* ", "Bichinho Virtual", "*")
print("*" * 20)

tamagushis = criar_tamagushi()

opcao = 1
while 0 <= opcao <= 3:
    opcao, tamagushi = menu_tamagushi(tamagushis)
    opcao = menu_principal(tamagushi)
