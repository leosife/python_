class Carro:
    def __init__(self,nome):
        self.nome = nome
        self.motor = None
        self.fabri =  None

    def motordocarro(self,motor):
        self.motor = motor

    def meufabri(self,fabricante):
        self.fabri = fabricante

class Motor:
    def __init__(self,nome):
        self.nome = nome


class Fabricante:
    def __init__(self,nome):
        self.nome = nome
        self.meuscarros = []

    def produzidos(self,car):
        self.meuscarros.append(car)
        

    def listar(self):
        for c in self.meuscarros:
            print (c)


carro1 = Carro('Focus')
motor1 = Motor('v3')
fabricante1 = Fabricante('Ford')


fabricante1.produzidos(carro1.nome)
carro1.motordocarro(motor1.nome)
carro1.meufabri(fabricante1.nome)
print(carro1.nome, carro1.motor, carro1.fabri)