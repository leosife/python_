def ctof(x):
    celsius = (x-32)*(5/9)
    return celsius
def ftoc(x):
    fah = (x*9/5) + 32
    return fah


print('Press C to convert from Fahrenheit to Celsius.\n'
    'Press F to convert from Celsius to Fahrenheit. ')
escolha = input('Your Choice: ')

if escolha in 'Cc':
    valor = float(input('Please enter the temperature in Fahrenheit:'))
    print(ctof(valor))

    ...
elif escolha in 'Ff':
    valor = float(input('Please enter the temperature in Celsius:'))
    print(ftoc(valor))
