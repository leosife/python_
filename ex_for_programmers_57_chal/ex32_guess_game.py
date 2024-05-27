import random
print('''Difficult: 
          1 - Easy(10 numbers)
          2 - Moderate(100 numbers)
          3 - Hard(1000 numbers)''')

while True:
    d = input('Your choice: ')
    match d:
        case '1':
            qtd = 10
        case '2':
            qtd = 100
        case '3':
            qtd = 1000
        case _:
            print('pick a valid option')
            continue
    break

c = 0
n = random.randint(1,qtd)
k = set()
while True:
    try:
        g = int(input('Qual o numero que estou pensando?: '))
    except ValueError:
        print('Digite um numero inteiro para continuar')
        c += 1
        continue
    if g in k:
        print('Ta maluco? voce ja chutou esse numero')
        c += 1
        continue
    else:
        k.add(g)
    if g == n:
        c += 1
        if c == 1:
            print( 'Voce le mentes? Acertou de primeira')
        elif c < 4:
            print( f'Estou impressionado, acertou em {c} tentantivas')
            
        elif c < 6:
            print(f'{c} tentativas? Achei que voce acertaria antes')
        else:
            print(f'Puhhh mais sorte da proxima vez,{c} tentativas no total')
        break
    elif g < n:
        print('O numero que estou pensando é maior')
    elif g > n:
        print('O numero que estou pensando é menor')
    c += 1
