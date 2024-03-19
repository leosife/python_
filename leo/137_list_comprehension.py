produtos = [
    {'nome':'p1','preco':10},
    {'nome':'p2','preco':20},
    {'nome':'p3','preco':30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.2} 
    if produto['preco'] < 25 else {**produto}
    for produto in produtos
]
novos_produtos.sort
print(*novos_produtos, sep='\n')