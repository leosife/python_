def soma_lista(l1,l2):
    intervalo = min(len(l1),(len(l2)))
    return [
        l1[i] + l2[i] for i in range(intervalo)
    ]

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5,6,7,8,9,10]
print(soma_lista(lista1,lista2))