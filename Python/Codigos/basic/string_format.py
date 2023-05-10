"""
format() é usado para combinar string e numeros.
Ele pega os argumentos numericos passados, formata e insere dentro dos placeholders {}
"""

idade = 33
texto = "Meu nome é jhon, e eu tenho {}"
print(texto.format(idade))

#Não tem limite de numeros que podem ser passados, preenchendo da esquerda para direita
qtd = 3
itemno = 890
preco = 49.50
pedido = "Eu quero {} unidades do item {} por {} reais"
print(pedido.format(qtd, itemno, preco))

#Também podemos usar o indice para indicar
pedido = "Eu quero pagar {2} reais por {0} unidades do item {1}"
print(pedido.format(qtd, itemno, preco))