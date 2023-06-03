""""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""


class Tamagushi:

    def __init__(self, nome: str, fome: int = 50, saude: int = 50, idade: int = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def humor(self, fome: int, saude: int):
        if fome >= 50 and saude >= 50:
            nome = self.nome
            print(f"{nome} está de bom humor")
        elif fome < 50 and saude < 50:
            nome = self.nome
            print(f"{nome} está de mau humor")

    def alimentar(self):
        self.fome += 10
        print(f"{self.nome} foi alimentado, agora sua fome é de: {self.fome}")
        if self.fome > 80:
            self.idade += 1
            self.fome = 50
            print(f"{self.nome} acaba de ficar 1 ano mais velho(a)")


