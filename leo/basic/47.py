n = input('Digite seu nome: ')
i = input('Digite sua idade: ')
if n and i != '':
    print(f'Seu nome é {n}')
    print(f"Seu nome invertido é {n[::-1]}")
    if ' ' in n:
        print('O nome contem espaços')
    print(f'O nome tem {len(n)} letras')
    print(f'A primeira letra do seu nome é {n[0]}')
    print(f'A primeira letra do seu nome é {n[-1]}')
else:
    print('Desculpe voce deixou campos em branco')
