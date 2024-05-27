from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,agencia,conta):
        self.agencia = agencia
        self.numeroconta = conta
        self.saldo = 0
      
    def depositar(self,valor):
        self.saldo += valor

    @abstractmethod
    def sacar():
        ...
class ContaCorrente(Conta):
    def sacar(self,valor):
        if valor <= self.saldo+500:
            if valor > self.saldo:
                print('voce uso seu limite')
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

class ContaPoupanca(Conta):
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')