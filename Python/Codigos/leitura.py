# with open(file="Python_M2_support material02.ipynb", mode='r', encoding='utf8') as arquivo:
#     conteudo = arquivo.read();
# print(conteudo)

conteudo = []

with open(file="Python_M2_support material02.ipynb", mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()
    while linha:
        conteudo.append(linha)
        linha = arquivo.readline()

# print(conteudo)
for linha in conteudo:
    print(linha.rstrip())  # Retira os '\n' da linha
