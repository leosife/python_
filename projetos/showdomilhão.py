import random
print('Bem Vindo ao Show do Milhão')

perguntas = [
    ['1-Um homem calvo é popularmente chamado de ?',
    '1) Careca','2) Cabeludo','3) Corno','4) maluco','1'],
    ['2 Com apenas 17 anos, Pelé foi campeão mundial de futebol na Copa de 1958 usando a camisa número:',
        '1) 9','2) 11','3) 10','4) 7','3']
 
  ]      
jafoi = set()
def question():

    print(perguntas[p][0],'\n',
    perguntas[p][1],'\n',
    perguntas[p][2],'\n',
    perguntas[p][3],'\n',
    perguntas[p][4])
 
         
   
while True:
    p = (random.randint(0,len(perguntas)-1))     
    if p in jafoi:
        if len(perguntas) == len(jafoi):
            break
        else:
            continue
    else:
        jafoi.add(p)
        question()   
        resp = input('Resposta[1/2/3/4]: ')
        print(perguntas[p][5])
        if perguntas[p] == perguntas[p][5]:
            print('Resposta Correta')
            continue
        else:
            print('Voce perdeu')
            break
           
        




