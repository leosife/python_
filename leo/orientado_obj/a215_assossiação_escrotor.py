class Escritor:
    def __init__(self,nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,valor):
        self._ferramenta = valor



class FerramentaDeEscrever:
    def __init__(self,nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} esta escrevendo'

escritor = Escritor('leo')
caneta = FerramentaDeEscrever('caneta bic')
maquina_de_escrever = FerramentaDeEscrever('maquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(escritor.ferramenta.escrever())
