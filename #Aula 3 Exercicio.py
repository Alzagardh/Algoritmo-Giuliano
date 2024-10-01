#Aula 3 Exercicio
clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)

def exibir_clientes():
    for cliente in clientes:
        print(f"Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")
            return
    print("Cliente não encontrado.")

def remover_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print("Cliente removido com sucesso.")
            return
    print("Cliente não encontrado.")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Cliente")
    print("2. Exibir Clientes")
    print("3. Buscar Cliente por E-mail")
    print("4. Remover Cliente")
    print("5. Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        adicionar_cliente(nome, email, telefone, endereco)
    elif opcao == '2':
        exibir_clientes()
    elif opcao == '3':
        email = input("Digite o e-mail do cliente: ")
        buscar_cliente(email)
    elif opcao == '4':
        email = input("Digite o e-mail do cliente: ")
        remover_cliente(email)
    elif opcao == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
