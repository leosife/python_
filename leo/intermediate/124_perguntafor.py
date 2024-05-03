p = [{
        'Pergunta':'(01) Quanto é 3 x 3?',
        'Opções':['3','2' ,'9', '6'],
        'Respostas':'9',
    },
    {
        'Pergunta':'(02) Quanto é 15 / 3?',
        'Opções':['5','16' ,'10', '25'],
        'Respostas':'5',
    },
    {
        'Pergunta':'(03) Quanto é 2 x 3?',
        'Opções':['3','2' ,'9', '6'],
        'Respostas':'6',
    }     ]
letra = ['a','b','c','d']
tentativas = 0

while True:
    print('*'*42)
    print('BEM VINDO AO JOGO DE PERGUNTAS E RESPOSTAS')
    print('*'*42)
    for i in range(1,len(p)+1):
        print(p[i-1]['Pergunta'])
        c = 0
        for alternativas in (p[i-1]['Opções']):
            print(f'{letra[c]})',alternativas)
            c += 1
        while True:  
            r = input('Resposta: ')
            if r == p[i-1]['Respostas']:
                print('Voce acertou')
                print('-'*20)
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
            break       
    if tentativas != 2:
        print('$'* 15)
        print('PARABENS VC GANHOU')
        print('$'* 15)
    nv = input('Digite sim para jogar novamente: ')
    if nv == 'sim':
        continue
    else:
        break
