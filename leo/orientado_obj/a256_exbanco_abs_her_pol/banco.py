
class Banco():
    val = False
    ag = '112'
    clientes = ['Carlos','Miguel','Maria', 'Joana']
    todasascontas = ['121216-5', '121216-6','121216-7', '121216-8']
    def Checarcliente(self,cliente,agencia,conta):
        if agencia == self.ag:
            if cliente in self.clientes and conta in self.todasascontas:
                    print(f'Bem vindo {cliente}')
                    return self.val == True
            else:
                print('Cliente ou conta não são validas')
        else:
            print('agencia errada')