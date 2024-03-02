def criar_mult(multiplicador):
    def multiplicar(numero):
        return multiplicador*numero
    return multiplicar

duplicar = criar_mult(2)
triplicar = criar_mult(3)
quadriplicar = criar_mult(4)

print(duplicar(5))
print(triplicar(5))
print(quadriplicar(5))