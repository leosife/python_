import os
palavra = 'sapato'
letrasacertadas = ''
c = 0
while True:
    t = input('digite uma letra: ')
    c += 1
    if len(t) > 1:
        print('Digite apenas uma letra')
        continue

    if t in palavra:
        letrasacertadas += t
    palavra_formada = ''
    for letra in palavra:
        if letra in letrasacertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)
    
    if palavra_formada == palavra:
        os.system('cls')
        print('Voce acertou a palavra')
        print('A palavra secreta era', palavra)
        print(f'Voce precisou de {c} tentativas')
        letrasacertadas = ''
        c = 0
        



    if t == 'sair':
        break