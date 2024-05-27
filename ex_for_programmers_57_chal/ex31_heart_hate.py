while True:
    try:
        age = int(input('Age: '))
        resting = int(input('Resting Pulse: '))
    except ValueError:
        print('Digite um numero inteiro')
        continue
    break


x = ((220-age)-resting)

for intensity in range(55,100,5):
    thr = (x*intensity)/100 + resting
    print(intensity,f' - {thr}')