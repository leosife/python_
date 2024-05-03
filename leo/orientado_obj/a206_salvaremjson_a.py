import json
caminho ='C:\\Users\\leo_s\\OneDrive\\Documentos\\projeto\\python_\\leo\\orientado_obj\\a206.json'

class Pessoa:
    def __init__(self,nome,idade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

p1 = Pessoa('joão', 22, 80)
salve = vars(p1)

with open(caminho,'w+',encoding='utf8') as arquivo:
    dados = json.dump(salve,arquivo,indent=2,ensure_ascii=False)
