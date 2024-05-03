def executa(funcao,b,c):
    return(funcao(c,b))

print(executa(lambda x,y: x + y,'Ola ','Mundo '))