# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self):
        print(self.__class__.__name__)


class Cliente(Pessoa):
    ...

class Aluno(Pessoa):

    def estudar(self):
        print('Estou estudando')

c1 = Cliente('João','Paulo')
a1 = Aluno('Marcos', 'Silva')
c1.falar()
a1.falar()
a1.estudar()
print(a1.nome)