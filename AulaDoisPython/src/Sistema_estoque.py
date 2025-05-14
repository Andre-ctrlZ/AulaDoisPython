def menu():
    while True:
        print("\n ---- MENU ---- ")
        print("1 - Adicionar item: ")
        print("2 - Listar items: ")
        print("3 - Alterar item: ")
        print("4 - Excluir item: ")
        print("5 - Sair: ")

        opcao = input("Digite uma opção: ")
        if opcao == "1":
            print("Chama função Adicionar item")
        elif opcao == "2":
            print("Chama a função Listar items")
        elif opcao == "3":
            print("Chama a função Alterar item")
        elif opcao == "4":
            print("Chama a função Excluir item")
        elif opcao == "5":
            break
        else:
            print("Opção inválida")