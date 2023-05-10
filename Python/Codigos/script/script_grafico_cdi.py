import csv
from sys import argv

import seaborn as sns

#Extraindo as colunas hora e taxa

horas = []
taxas = []

with open(file='./script/taxa-cdi.csv', mode='r', encoding='utf8') as fp:
    linha = fp.readline()
    linha = fp.readline()
    while linha:
        linha_separada = linha.split(sep=',') #transformando em array e seprando cada elemento q contem virgula.
        hora = linha_separada[1] #linha_separada é um array com indice, como qualquer outro, por isso está pegando o conteudo do indice 1 que são as horas
        horas.append(hora)
        taxa = float(linha_separada[2]) #linha_separada é um array com indice, como qualquer outro, por isso está pegando o conteudo do indice 2 que são as taxas e transformando para float
        taxas.append(taxa)
        linha = fp.readline() #Atualiza a linha para verificar se existe a proxima, caso não exista sairá do while.

#Salvando no grafico

grafico = sns.lineplot(x=taxas, y=horas)
grafico.get_figure().savefig(f"{argv[1]}.png")