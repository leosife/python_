lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

cubo = [
    lista[i]**3  for i in range(len(lista)) if lista[i]%2 != 0
]


print(cubo)