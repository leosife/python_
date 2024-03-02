n = input('Digite um numero inteiro: ')

if n.isnumeric():
    n = int(n)
    if n % 2 == 0:
        print(f'O numero {n} é par')
    else:
        print(f'O numero {n} é impar')

else:
    print('Voce não digitou um numero inteiro')

nome = input('Qual seu nome?: ')
h = int(input('Que horas são?: '))

if h >= 0 and h <= 11:
    print('Bom dia, ',"\n")
elif 12 <= h <=17:
    print('Boa Tarde')
elif 17 <= h <=23:
    print('Boa noite')


if len(nome) <= 4:
    print(f'Seu nome é muito curto {nome}')
elif len(nome) > 4 and len(nome) < 7:
    print(f'Seu nome é normal {nome}')
else:
    print(f'Seu nome é muito grande {nome}')




