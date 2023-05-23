from tamagushi import Tamagushi

print("*" * 20)
print("* ", "Bichinho Virtual", "*")
print("*" * 20)
nome = input("Qual o nome que você deseja para seu novo pet?")

t1 = Tamagushi(nome=nome, fome=50, idade=0, saude=50)
t1.humor(t1.fome, t1.saude)

menu = int(input("""
Digite 1 para alimentar
Digite 2 para verificar o humor do pet
Digite 3 para verificar a saude
Digite 4 para Verificar a fome
Digite 5 para verificar a idade
"""))


while 0 < menu <= 5:
    if menu == 1:
        t1.alimentar()
    elif menu == 2:
        t1.humor(t1.fome, t1.saude)
    elif menu == 3:
        print("de 0 a 100 a saude está em: ", t1.saude)
    elif menu == 4:
        print("de 0 a 100 a fome está em: ", t1.fome)
    elif menu == 5:
        print(f"{t1.nome} tem {t1.idade} anos")
    menu = int(input("""
Digite 1 para alimentar
Digite 2 para verificar o humor do pet
Digite 3 para verificar a saude
Digite 4 para Verificar a fome
Digite 5 para verificar a idade
"""))