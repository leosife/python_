import re
def check_name(n):
    if len(n) == 0:
        return 'O campo deve ser preenchido'
    if n.isalpha():
        if len(n) <= 2:
            return f'O nome {n} não é valido, pois é muito curto'
    else:
        return 'Seu nome deve conter apenas letras'
    return True

def check_lname(n):
    if len(n) == 0:
        return 'O campo deve ser preenchido'
    if n.isalpha():
        if len(n) <= 2:
            return f'O Sobrenome {n} não é valido, pois é muito curto'
    else:
        return 'Seu Sobrenome deve conter apenas letras'
    return True

def checkid(id):
    if len(id) != 8:
        return 'O seu ID deve conter 8 digitos - Sendo AA-00000'
    for i in range(len(id)):
        if i <= 1:
            if id[i].isalpha() == False:
                return 'Seu ID deve conter duas letras iniciais'
        elif i == 2:
            if id[i] != '-':
                return 'Seu ID deve conter um - apos as duas letras iniciais'
        elif i < 7:
            if id[i].isnumeric() == False:
                return 'Seu ID deve conter 5 numeros apos o - '
    return True
def checkzip(zipi):
    if zipi.isnumeric() == False:
        return 'O seu codigo ZIP deve ser um numero'
    return True

def validation(thing):
    if thing is name:
        return check_name(thing)
    elif thing is lname:
        return check_lname(thing)
    elif thing is id:
        return checkid(thing)
    elif thing is zipi:
        return checkzip(thing)


while True:
    name = input('Name: ')
    if validation(name) != True:
        print(validation(name))
        continue

    lname = input('Last Name: ')
    if validation(lname) != True:
        print(validation(lname))
        continue
    id = input('Employee ID: ')
    if validation(id) != True:
        print(validation(id))
        continue
    zipi = input('ZIP Adress: ')
    if validation(zipi) != True:
        print(validation(zipi))
        continue
    break
print('Cadastro Efetuado')


