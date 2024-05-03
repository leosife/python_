import json
from a206_salvaremjson_a import caminho, Pessoa



with open(caminho,'r') as arquivo:
    pessoas = json.load(arquivo)

print(pessoas)
p1 = Pessoa(**pessoas)


print(p1.nome)