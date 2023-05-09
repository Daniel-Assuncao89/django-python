from pessoa import Pessoa
from universidade import Universidade


class Funcionario(Pessoa):

    def __init__(self, nome: str, idade: int, documento: str, cargo: str , universidade: Universidade):
        super().__init__(nome=nome, idade=idade, documento=documento)
        self.cargo = cargo
        self.universidade = universidade