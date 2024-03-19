import random
times = ['Palmeiras','Santos','São Paulo','Corinthians','Gremio','Inter','Flamengo','Vasco',
         'Cruzeiro','Atletico-MG','Ceara','Fortaleza','Bahia','Vitoria','Bragantino','Fluminense'
         ]
random.shuffle(times)
gol = []



while len(times) != 1:
    qtd_d_times = len(times)
    les = []
    qtd_jogos = int(qtd_d_times/2)

    for time in range(qtd_d_times):
        gol.append(random.randint(1,4))
    
    for i in range(qtd_jogos):
        
        print(f'{times[i]} {gol[i]} x {gol[-i-1]} {times[-i-1]}')
        if gol[i] > gol[-i-1]:
            v = times[i]
            les.append(v)
            
        elif gol[i] < gol[-i-1]:
            les.append(times[-i-1])
            
        else:
            pen = (times[i],times[-i-1])
            a = random.choice(pen)
            les.append(a)
            print(f'-----PENALTIS - vencedor {a}')
    
    times = les
    print('')
    

    if len(times) == 1:
        print('#'*30)
        print(*times, end='')
        print(f' Campeão da copa Python')
        print('#'*30)
        print('')
    elif len(times) == 4:
        print('Semi-Final')
        print(times)
    else:
        print(times)



   








# for time in times:
#     g = random.randint(1,4)
#     time0 = 
#     print(time, g)

#     if 