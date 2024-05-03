import os
while True:
    senha = input('Crie sua senha: ')
    if len(senha) == 0:
        os.system('cls')
        print('Digite uma senha')
        continue
    if len(senha) < 8:
        print('senha muito fraca')
    elif senha.isdigit():
        print('senha muito fraca')
    elif senha.isalpha():
        print('senha fraca')
    # elif senha.isalnum() and len(senha) > 8:
    #     print('senha boa')
    elif any(n.isdigit() for n in senha):
        if any(n.isalpha() for n in senha):
            print('sua senha tem numero e letra')