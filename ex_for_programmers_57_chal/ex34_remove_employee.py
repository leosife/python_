e =['John Smith',
'Jackie Jackson',
'Chris Jones',
'Amanda Cullen',
'Jeremy Goodwin']
lista = 'C:\\Users\\leo_s\\OneDrive\\Documentos\\projeto\\python_\\ex_for_programmers_57_chal\\func.txt'
removee = input('Remove name: ')
try:
    e.remove(removee)
except ValueError:
    print('Name not found')
print(e)

with open(lista,'w',encoding='utf8') as arquivo:
    for name in e:
        arquivo.write(name)
        arquivo.write('\n')