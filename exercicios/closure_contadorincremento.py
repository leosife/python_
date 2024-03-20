def criar_contador_incremento(inicial,incremento):
    contador = inicial
    def contador_interna():
        nonlocal contador
        valor_atual = contador
        contador += incremento
        return valor_atual
    return contador_interna

contagem1 = criar_contador_incremento(0,7)
contagem2 = criar_contador_incremento(0,2)
        
print(contagem2())
print(contagem2())
print(contagem2())
print(contagem2())

print(contagem1())
print(contagem1())
print(contagem1())
print(contagem1())