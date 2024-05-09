palavra = 'dinossauro'
pc = []
s1 = set()

print(f'A palavra tem {len(palavra)} letras')
while True:
    palavra_correta = ''
    chute = input('Qual letra deseja chutar?: ')
    if chute.isnumeric():
        print('digite uma letra')
        continue
    pc.append(chute)
    if chute in palavra:
        s1.add(chute)
    print(f'letras chutadas {pc}')
    for l in palavra:
        if l in s1:
            palavra_correta += l
        else:
            palavra_correta += '_'
    print(palavra_correta)

    if palavra_correta == palavra:
        print('Parabens voce acertou')
        break
        