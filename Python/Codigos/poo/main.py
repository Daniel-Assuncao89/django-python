from pessoa import Pessoa
import universidade
import funcionario

#Metodo para validar se é maior de idade
def maior_de_idade(idade: int) -> bool:
    return idade >= 18


#Instanciando 3 objetos de pessoa
andre = Pessoa(nome="Andre Perez", idade=30, documento="123")
maria = Pessoa(nome="Maria Perez", idade=56, documento="456")
pedro = Pessoa(nome="Pedro Perez", idade=8)
print(andre.nome)


if maior_de_idade(idade=andre.idade):
    print(f"{andre.nome} é maior de idade")

#abrindo um dict e vinculando um score a cada documento
score_credito = {'123': 750, '456': 812, '789': 327}
score = score_credito[andre.documento]
print(score)

andre.dormir(horas=2)
andre.falar(texto="Olá pessoal")

print(andre)

#Instanciando uma universidade
usp = universidade.Universidade(nome="Universidade de São Paulo")

andre = funcionario.Funcionario(nome="Andre Perez", idade=30, documento='123',cargo='Eng. software', universidade=usp)

print(andre.universidade.nome)