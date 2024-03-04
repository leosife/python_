def executa(funcao, *args):
    return funcao(*args)


d = executa(
        lambda x,y: x*y,
        4, 5
        )

print(d)