import os
clientes =[]     # -> clientes=[]
fornecedores= [] #-> fornecedores =[]
pecas =[]       #-> pecas=[]

while True: # NÃO TEM CONDICIONAL
    print('Selecione uma opção: ') #SEM ASPAS
    print('1 - Cadastrar cliente') #SEM ASPAS
    print('2 - Cadastrar fornecedor ')#SEM ASPAS
    print('3 - Cadastrar peça ')#SEM ASPAS
    print('4 - Gerar relatório ')#SEM ASPAS
    print('5 - Sair ')#SEM ASPAS

    opcao = input("Opção selecionada: ") #-> o sinal =
    os.system(cls)
    try: #NÃO ESTAVA INDENTADO
            opcao = int(opcao)
    except ValueError: #excepet
        print("Opção inválida. Por favor, digite um número.")
        continue

    if opcao == 1: #sem sinal de :
        nome = input("Digite o nome do cliente: ")  #->input
        telefone = input("Digite o telefone do cliente: ") #->input
        endereco = input("Digite o endereço do cliente: ") #->input
        clientes.append({"nome": nome, "telefone": telefone, "endereco": endereco})
        print("Cliente cadastrado com sucesso!")

    elif opcao == 2:# NÃO ESTÁ INDENTADO
        nome = input("Digite o nome do fornecedor: ")
        telefone = input("Digite o telefone do fornecedor: ")
        endereco = input("Digite o endereço do fornecedor: ")
        fornecedores.append({"nome": nome, "telefone": telefone, "endereco": endereco})
        print("Fornecedor cadastrado com sucesso!")

#colocar um while pq perde qdo digitado diferente
    elif opcao == 3:
        nome = input("Digite o nome da peça: ")
        fornecedor = input("Digite o nome do fornecedor da peça: ")
        preco = float(input("Digite o preço da peça: "))
    
        try:
            preco = float(preco)
        except ValueError:
            print("Preço inválido. Por favor, digite um número.")
            continue

        pecas.append({"nome": nome, "fornecedor": fornecedores, "preco": preco}) #fornecedor 
        print("Peça cadastrada com sucesso!")

    elif opcao == 4:
        print("Relatório de clientes:")
        for cliente in clientes:
                print(f"Nome: {cliente['nome']}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")
                print()

        print("Relatório de fornecedores:")
        for fornecedor in fornecedores:
                print(f"Nome: {fornecedor['nome']}, Telefone: {fornecedor['telefone']}, Endereço: {fornecedor['endereco']}")
                print()

                print("Relatório de peças:")
        for peca in pecas:
            print(f"Nome: {peca['nome']}, Fornecedor: {peca['fornecedor']}, Preço: {peca['preco']}")
            print()
            os.system('pause')
    elif opcao == 5:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
                
    # 35 erros