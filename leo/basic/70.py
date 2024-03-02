frase = 'Eu te amo muito minha panquequinha'
letramais = ''
qtdapareceu = 0

i = 0
while i < len(frase):

    
    latual = frase[i]
    i += 1
    if latual == ' ':
        continue
    if qtdapareceu < frase.count(latual):
        letramais = latual
        qtdapareceu = frase.count(latual)


print(letramais)
print(qtdapareceu)

