def is_primo(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    elif x == 5 or x == 7:
        return True
    for i in range(2,10):
        if x % i == 0:
            return False
    else:
        return True
    
print(is_primo(31))

primos = [
        x for x in range(1,51) if is_primo(x)

]
print(primos)
