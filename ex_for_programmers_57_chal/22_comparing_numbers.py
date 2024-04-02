
# while True:
#     n1 = int(input('Primeiro numero: '))
#     n2 = int(input('Segundo numero: '))
#     n3 = int(input('Terceiro numero: '))

#     if n1 == n2 or n1 == n3 or n2 == n3:
#         print('voce digitou numeros iguais')
#     else:
#         if n1 > n2 and n1 > n3:
#             print(n1)
#         elif n2 > n1 and n2 > n3:
#             print(n2)
#         elif n3 > n1 and n3 > n2:
#             print(n3)

sete = set()
while True:
    if len(sete) == 10:
        break
    
    n = int(input('Digite um numero: '))
    if n in sete:
        print('O numero ja foi adicionado')
        continue
    else:
        sete.add(n)

print(sete)
print(max(sete))