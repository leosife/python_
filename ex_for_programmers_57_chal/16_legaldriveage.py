idadedirigir = 18
idadepaises = {'Brasil':18,'Eua': 16, 'China':21,'Inglaterra':17,'Nao existe': 7}

pode = []

try:
    idade = int(input('Qual sua idade: '))
    if idade <= 0:
        print('Digite uma idade valida')
    else:
        for v in idadepaises:                
            if idade >= idadepaises[v]:
                pode.append(v)
        print(f'Com {idade} anos, voce pode dirigir nos paises: ')
        for p in pode:
            print(p)
except ValueError:
    print('Digite um numero valido')

