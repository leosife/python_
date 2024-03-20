def potencia_parcial(expoente):
    def potencia(x):
        result = pow(x,expoente)

        return result
    return potencia


expoente = potencia_parcial(3)

print(expoente(2))
print(expoente(3))
print(expoente(4))
