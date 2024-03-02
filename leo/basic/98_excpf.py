import re
import sys  

cpfd = input('cpf: ')
cpf = re.sub(r'[^0-9]','',cpfd)

entrada_seq = cpfd == cpfd[0]*len(cpfd)
if entrada_seq:
    sys.exit()

cpf1 = cpf[:9]
c1 = 10
soma1 = 0

for n in cpf1:
    a = int(n)
    soma1 += a*c1
    c1 -= 1
print(soma1)

result1 = ((soma1*10) % 11)

result1 = result1 if result1 <= 9 else 0
print(result1)

cpf2 = cpf[:10]
c2 = 11
soma2 = 0

for n in cpf2:
    b = int(n)
    soma2 += b*c2
    c2 -= 1
print(soma2)

result2 = ((soma2*10) % 11)
result2 = result2 if result2 <= 9 else 0
print(result2)

cpf_gerado = f'{cpf1}{result1}{result2}'


if cpf_gerado == cpf:
    print('CPF valido')
else:
    print('CPF invalido')