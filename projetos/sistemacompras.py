import json
caminho = 'C:\\Users\\leo_s\\OneDrive\\Documentos\\projeto\\python_\\projetos\\sistema_qtd.json'
caminho2 = 'C:\\Users\\leo_s\\OneDrive\\Documentos\\projeto\\python_\\projetos\\sistema_preco.json'
class Armazem:
    def __init__(self):
        self.quantidade = {}
        self.preco = {}

    def novoItem(self,nome,qtd,preco):
        self.quantidade[nome] = qtd
        self.preco[nome] = preco
   
    def atualizarItem(self,nome,qtd):
        a = self.quantidade[nome]
        b = a + qtd
        self.quantidade[nome]  = b

    def listarItem(self):
        for i, v in self.quantidade.items():
            print('*'*40)
            print(f'Item: {i:<15} Qtd:{v:<5} Preço:{self.preco[i]}')

    def salvar(self):
        lista = self.quantidade
        lista2 = self.preco
        with open(caminho,'w+',encoding='utf8') as arquivo:
            dados = json.dump(lista,arquivo,indent=2)
        with open(caminho2,'w+',encoding='utf8') as arquivo:  
            dados2 = json.dump(lista2,arquivo,indent=2)
    


        

arm = Armazem()

with open(caminho, 'r',encoding='utf8') as arquivo:
    arm.quantidade = json.load(arquivo)
with open(caminho2, 'r',encoding='utf8') as arquivo:
    arm.preco = json.load(arquivo)
while True:

    print('__'*10)
    opc = input('''[1] Adicionar Item 
[2] Listar Itens 
[3] Baixa Item 
[4] Salvar alterações: ''')
    match opc:
        case '1':
            i = input('item: ')
            try:
                q = int(input('quantidade: '))
            except ValueError:
                print('ERRO - Digite a quantidade correta')
            if i in arm.preco.keys():
                arm.atualizarItem(i,q)
                print('item adicionado')
            else:
                try:
                    print('item novo adicione o preco')
                    preco = float(input('Preço: '))
                    print('Novo produto cadastrado')
                    arm.novoItem(i,q,preco)
                except ValueError:
                    print('ERRO - Digite um valor valido ex 0.00')

        case '2':
            arm.listarItem()
        case '3':
            ir = input('item: ')
            try:
                qr = int(input('quantidade: '))
            except ValueError:
                print('ERRO - Digite a quantidade correta')
            arm.atualizarItem(ir,-qr)

        case '4':
            arm.salvar()
            print('Alterações salvas')

