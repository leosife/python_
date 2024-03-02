import os
lst = []

while True:
    print('Selecione uma opção')
    escolha = input('[i]nserir, [a]pagar, [m]ostrar, [s]air: ' )
    if  escolha == 's':
        break
    elif escolha == 'i':
        add = input('Qual item: ')
        lst.append(add)
        os.system('cls')
        print(f'{add} adicionado a lista')
    elif escolha == 'a':
        apg = int(input('Qual o indicice para apagar: '))
        os.system('cls')
        try:
            lst.pop(apg)
            print(f'item {apg} apagado da a lista')
        except:
            print('indice invaldio')
            continue
    elif escolha =='m':
        os.system('cls')
        for i,item in enumerate(lst):
            print(i,item)
    else:
        os.system('cls')
        print('Voce digitou uma opção invalida')
        
        continue
