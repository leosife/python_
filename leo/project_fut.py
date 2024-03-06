import random

r1 = ["Time A", "Time B", "Time C", "Time D"]
r2 = ["Time D", "Time A", "Time B", "Time C"]
r3 = ["Time A", "Time C", "Time B", "Time D"]


def simular_confronto(rodada):
    # Gerando um placar aleatório para o confronto
    c = 0
    for i in range(2):
        placar_time1 = random.randint(0, 5)
        placar_time2 = random.randint(0, 5)
        print(f'{rodada[c]} {placar_time1} x {placar_time2} {rodada[c+1]}')
        c += 2
    return placar_time1, placar_time2
print(simular_confronto(r1))


