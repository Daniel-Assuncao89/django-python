"""
Strings são arrays em Python representando unicode caracter
Pyhton não possui o tipo 'char', ele é simplesmente uma string
de tamanho 1
"""

variavel = " Paralelepipedo do gepeto da macedonia "

#diferente do java, no python obtemos pelo 'len' o tamanho do array
print(len(variavel))

#Verificar se uma palavra está dentro de uma string. Retorna um booleano
print("do" in variavel)

#Também temos o se não está contido na string
print("do" not in variavel)

#Por ser um array, podemos usar o loop normalmente
for char in variavel:
    print(char)

print(variavel.upper())
print(variavel.lower())

#Remover espaços em branco do inicio e/ou do final da string
print(variavel.strip())

#Replace string
print(variavel.replace(" ", "!"))

#Split quebra no separador indicado e retorna uma lista
print(variavel.split(" "))