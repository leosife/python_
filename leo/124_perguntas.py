import os
while True:
    print('*'*30)
    print('BEM VINDO AO JOGO DE PERGUNTAS E RESPOSTAS')
    print('*'*30)
    tentativas = 0

    print('(01) Quanto é 3 x 3?')
    print('''Opções:
            a) 3
            b) 2
            c) 9
            d) 6
            ''')

    while True:
        r1 = input('Resposta: ')

        if r1 in '9d':
            print('Voce acertou')
            tentativas = 0
            break
        else:
            print('Resposta incorreta')
            tentativas += 1

            if tentativas == 1:
                print('Voce tem mais uma chance')
            if tentativas == 2:
                print('Voce perdeu')
                
                break
    if tentativas == 2:
        tentar = input('Digite sim para tentar outra vez: ')
        if  tentar == 'sim':
            os.system('cls')
            continue
            
        else:   
            break

    print('(02) Quanto é 15 / 3?')
    print('''Opções:
            a) 5
            b) 16
            c) 10
            d) 25
            ''')

    while True:
        r1 = input('Resposta: ')

        if r1 in '5a':
            print('Voce acertou')
            tentativas = 0
            break
        else:
            print('Resposta incorreta')
            tentativas += 1

            if tentativas == 1:
                print('Voce tem mais uma chance')
            if tentativas == 2:
                print('Voce perdeu')
                
                break
    if tentativas == 2:
        tentar = input('Digite sim para tentar outra vez: ')
        if  tentar == 'sim':
            os.system('cls')
            continue
            
        else:
            break

    print('(03) Quanto é 2 x 3?')
    print('''Opções:
            a) 3
            b) 2
            c) 9
            d) 6
            ''')

    while True:
        r1 = input('Resposta: ')

        if r1 in '6d':
            print('Voce acertou')
            tentativas = 0

            break
        else:
            print('Resposta incorreta')
            tentativas += 1

            if tentativas == 1:
                print('Voce tem mais uma chance')
            if tentativas == 2:
                print('Voce perdeu')
                
                break
    if tentativas == 2:
        tentar = input('Digite sim para tentar outra vez: ')
        if  tentar == 'sim':
            os.system('cls')
            continue
            
        else:   
            break

    print('(04) Quanto é 15 + 53?')
    print('''Opções:
            a) 52
            b) 64
            c) 68
            d) 70
            ''')

    while True:
        r1 = input('Resposta: ')

        if r1 == 'c' or r1 == '68':
            print('Voce acertou')
            vencedor = 'sim'
            break

        else:
            print('Resposta incorreta')
            tentativas += 1

            if tentativas == 1:
                print('Voce tem mais uma chance')
            if tentativas == 2:
                print('Voce perdeu')
                
                break
    if tentativas == 2:
        tentar = input('Digite sim para tentar outra vez: ')
        if  tentar == 'sim':
            os.system('cls')
            continue
            
        else:
            break

    if vencedor == 'sim':
        print('')
        print('$'*25)
        print('VOCE GANHOU O DESAFIO')
        print('$'*25)
        print('')
        break



