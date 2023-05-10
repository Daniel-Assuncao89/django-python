import os
import json
from datetime import datetime

import requests

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

data_e_hora = datetime.now()
data = datetime.strftime(data_e_hora, '%Y/%m/%d')
hora = datetime.strftime(data_e_hora, '%H:%M:%S')

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.HTTPError as  exec:
    print("Dado não encontrado, continuando.")
    cdi = None
except Exception as exec:
    print("Erro, parando a execução")
    raise exec
else:
    dado = json.loads(response.text) #Converte o json response.text em dict
    cdi = float(dado['taxa'].replace(',' , '.')) #Substituindo a virgula por ponto dentro do campo "taxa" e transformando esse dado em float

#Verificando se o arquivo cdi existe
if os.path.exists('taxa-cdi.csv') == False:
    with open(file='taxa-cdi.csv', mode='w', encoding='utf8') as fp:
        fp.write('data,hora,taxa,\n')

with open(file='taxa-cdi.csv', mode='a', encoding='utf8') as fp:
    fp.write(f'{data},{hora},{cdi},\n')
    print("Sucesso")