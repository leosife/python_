def linha(c,x=' '):
    print(f'{x:^2}',end='|')
    for i in range(13):
        print(f'{i*c:>4}',end=' ')
    print('')

contador = 0
linha(1)
for n in range(13):
    linha(contador,contador)
    contador += 1
