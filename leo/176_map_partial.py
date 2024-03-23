# map, partial, GeneratorType e esgotamento de Iterators
from functools import partial
from types import GeneratorType


#funcao para printar iterators
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

#funcao para aumentar a porcentagem
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

# partial funcao que recebe funcao A função partial permite consertar o número de argumentos de uma função 
# e até mesmo gerar uma nova função, essa função retorna uma função parcial, 
# que podemos dizer que é “quase” idêntica a original, mas dispõe de algumas alterações.
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def muda_preco_de_produtos(produto):
    return {
        **produto,'preco': aumentar_dez_porcento(produto['preco'])
    }

# map - para mapear dados
# list - esgota os iterador(permite vizualizar no print)
novos_produtos = list(map(muda_preco_de_produtos, produtos))


print_iter(produtos)
print_iter(novos_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)