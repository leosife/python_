# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(l1,l2):
    intervalo_max = min(len(l1),len(l2))
    print(intervalo_max)
    return [
        (l1[i],l2[i]) for i in range(intervalo_max)

    ]

print(zipper(lista1,lista2))