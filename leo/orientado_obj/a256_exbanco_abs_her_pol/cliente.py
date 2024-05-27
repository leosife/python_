
class Pessoa():
    def __init__(self, name, idade):
        self.name = name
        self.idade = None

    def __repr__(self) -> str:
        return self.name


class Cliente(Pessoa):
    def __init__(self, name, idade):
        super().__init__(name, idade)
        self.conta = None
