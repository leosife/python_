import copy
produtos = [
{'nome':'Produto 5','preco':10.00},
{'nome':'Produto 1','preco':22.32},
{'nome':'Produto 3','preco':10.11},
{'nome':'Produto 2','preco':105.87},
{'nome':'Produto 4','preco':69.90},
]

#aumentando 10% preco
novos_produtos = [
    {**produto, 'preco': round(produto['preco']*1.1,2)}
    for produto in produtos
]


print(*novos_produtos, sep='\n')
print('')

#ordenando por nome(decrescente)
produtos_ordenados_nome = sorted(copy.deepcopy(novos_produtos),key=lambda p:p['nome'],reverse=True)
print(*produtos_ordenados_nome,sep='\n')
print('')

#ordenando por preco

produtos_ordenados_preco = sorted(copy.deepcopy(novos_produtos),key=lambda p:p['preco'])
print(*produtos_ordenados_preco,sep='\n')