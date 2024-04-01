tarefas = []
apagados = []

def lista_itens(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa')
        return
    print('TAREFAS:')
    for i in tarefas:
        print(i,end='\n')
    print('')

while True:
    print('Comandos: listar, desfazer, refazer','sair')
    tarefa = input('Digite uma tarefa ou comando: ')
    if tarefa == 'sair':
        break

    if tarefa == 'listar':
        lista_itens(tarefas)

    elif tarefa == 'desfazer':
        apagados.append(tarefas.pop())
        lista_itens(tarefas)

    elif tarefa == 'refazer':
        tarefas.append(apagados.pop())
        lista_itens(tarefas)

    else:
        tarefas.append(tarefa)



