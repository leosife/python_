def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else: 
            baixo = meio + 1
    

minha_lista = [1, 3, 5, 7, 9,11,13,15,17,19,21] 
print(pesquisa_binaria(minha_lista, 21)) # => 1 
print(pesquisa_binaria(minha_lista, -1)) # => None 