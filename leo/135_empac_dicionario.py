dicio1 = {'Nome':'Leo','Idade':'27'}
dicio2 = {'Sobrenome':'Fernandes', 'Cor':'Verde'}

resultado = {**dicio1,**dicio2}

print(resultado)

def mostro_argumento_nomeados(*args,**kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumento_nomeados('ola',nome='Joana',idade=18)