# Create a simple program that validates user login credentials.
# The program must prompt the user for a username and
# password. The program should compare the password given
# by the user to a known password. If the password matches,
# the program should display “Welcome!” If it doesn’t match,2

# the program should display “I don’t know you.”
import getpass
import json
caminho_arquivo = 'C:\\Users\\leo_s\\OneDrive\\Documentos\\projeto\\python_\\ex_for_programmers_57_chal\\15arquivosalvo.json'

def ler(caminho_arquivo):
    dados = {}
    with open(caminho_arquivo, 'r',encoding='utf8') as arquivo:
        dados = json.load(arquivo)
    return dados

def cadastrar(login,senha):
    cad[login] = senha
    with open(caminho_arquivo,'w+',encoding='utf8') as arquivo:
        dados = json.dump(cad, arquivo, indent=2,ensure_ascii=False)
    

    print(cad)

cad = ler(caminho_arquivo)
print(cad)
while True:
    opcao = input('Digite 1 para logar ou 2 para cadastrar?')
    if opcao == '2':
        login = input('Login: ')
        senha = input('Senha: ')
        cadastrar(login,senha)
    if opcao == '1':
        logina = input('Login: ')
        senha = input('Senha: ')
        if logina in cad and cad[logina] == senha:
            print('Logado')
        else:
            print('login ou senhas incorretos')
        
    

# def cadastrar(log,sen):
    
#     cad[log] = sen
#     dados = cad
#     with open(caminho_arquivo,'w+',encoding='utf8') as arquivo:
#          dados = json.dump(cad, arquivo, indent=2,ensure_ascii=False)
        
# while True:      
#     cadastrar('lucaasasdaasasasass','meumalsdavado')
# login = input('Login: ')
# senha = getpass.getpass('Senha: ',)

# if senha == senha_correta:
#     print('Welcome')
# else:
#     print('Senha incorreta')
