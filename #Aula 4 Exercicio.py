#Aula 4 Exercicio
tarefas = []

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if lista_tarefas:
        novo_id = max(tarefa['id'] for tarefa in lista_tarefas) + 1
    else:
        novo_id = 1
    nova_tarefa = {
        'id': novo_id,
        'descricao': descricao,
        'status': status,
        'prioridade': prioridade
    }
    lista_tarefas.append(nova_tarefa)

def visualizar_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = []
    for tarefa in lista_tarefas:
        if (status is None or tarefa['status'] == status) and (prioridade is None or tarefa['prioridade'] == prioridade):
            tarefas_filtradas.append(tarefa)
    return tarefas_filtradas

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Filtrar Tarefas")
    print("4. Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        descricao = input("Digite a descrição da tarefa: ")
        status = input("Digite o status da tarefa (pendente, em andamento, concluída): ")
        prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ")
        adicionar_tarefa(tarefas, descricao, status, prioridade)
    elif opcao == '2':
        visualizar_tarefas(tarefas)
    elif opcao == '3':
        status = input("Digite o status para filtrar (ou deixe em branco para ignorar): ")
        prioridade = input("Digite a prioridade para filtrar (ou deixe em branco para ignorar): ")
        status = status if status else None
        prioridade = prioridade if prioridade else None
        tarefas_filtradas = filtrar_tarefas(tarefas, status, prioridade)
        visualizar_tarefas(tarefas_filtradas)
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
