def criar_contador(x):
    contador = x
    def contador_int():
        nonlocal contador
        valor_actual = contador
        contador += 1
        return valor_actual
    
    return contador_int


contador = criar_contador(5)

print(contador())
print(contador())
print(contador())
print(contador())
print(contador())
print(contador())
