import random

r1 = ["Time A", "Time B", "Time C", "Time D"]
r2 = ["Time D", "Time A", "Time B", "Time C"]
r3 = ["Time A", "Time C", "Time B", "Time D"]


def simular_confronto(time1, time2):
    # Gerando um placar aleatório para o confronto
    placar_time1 = random.randint(0, 5)
    placar_time2 = random.randint(0, 5)
    return placar_time1, placar_time2

def resultado(rodada):
    c = 0
    for i in range(2):
        print(rodada[c],' x ',rodada[c+1])
        c += 2

resultado(r1)