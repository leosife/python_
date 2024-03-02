while True:
    p1 = input('digite o primeiro numero: ')
    s1 = input('digite o segundo numero: ')
    o = input('Qual o operador(+,-,/,*): ')
    numeros_validos = None
    try:
        p = float(p1)
        s = float(s1)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos numeros são invalidos')
        continue

    if o not in '+-/*':
        print('Operador invalido')
        continue


    if o == '+':
        print(f'{p}+{s}={p+s}')
    elif o =='-':
        print(f'{p}-{s}={p-s}')
    elif o =='*':
        print(f'{p}x{s}={p*s}')
    elif o =='/':
        print(f'{p}/{s}={p/s}')

    nv = input('Calcular outro numero?[S/N] :').upper().startswith('N')
    if nv is True:
        break
