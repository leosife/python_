

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    print(total)

multiplica(1,2,3,4,5)

def parimpar(x):
    if x % 2 == 0:
        print(f'O numero {x} é par') 
    print(f'O numero {x} é impar')

parimpar(2223)

