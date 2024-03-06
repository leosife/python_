# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=11)
for n in gen:
    print(n)



def generator1(n=0, maximum=10):
    yield 1
    print('Ola')
    yield 2
    print('Eba')
    yield 3
    return 'ACABOU'
gen = generator1()
print(next(gen))
print(next(gen))
print(next(gen))
