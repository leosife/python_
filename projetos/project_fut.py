import random

r1 = ["Time A", "Time B", "Time C", "Time D"]
r2 = ["Time D", "Time A", "Time B", "Time C"]
r3 = ["Time A", "Time C", "Time B", "Time D"]
tabela = {'Time A':0,'Time B':0,'Time C':0,'Time D':0}

Timea = 0
timeb = 0

r1[0] = 1

def simular_confronto(rodada):
    # Gerando um placar aleatório para o confronto
    c = 0
    vencedores = []
    empate = []
    for i in range(2):
        
        placar_time1 = random.randint(0, 5)
        placar_time2 = random.randint(0, 5)
        print(f'{rodada[c]} {placar_time1} x {placar_time2} {rodada[c+1]}')

        if placar_time1 > placar_time2:
            vencedores.append(rodada[c])
        elif placar_time1 < placar_time2:
            vencedores.append(rodada[c+1])
        else:
            empate.append(rodada[c+1])
            empate.append(rodada[c])
            
        c += 2

        
    print(vencedores)
    print(empate)

print(simular_confronto(r1))


