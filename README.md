# sistema_de_placa
while True:
    print("\n--- SISTEMA DE PLACAS ---")
    print("1 - Adicionar Placas")
    print("2 - Consultar Placas")
    print("3 - Remover Placas")
    print("4 - Limpar Sistema")
    print("5 - Listar Sistema")
    print("0 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
        nova_placa = input("Digite a placa para adicionar: ")
        if nova_placa not in placas:
            placas.append(nova_placa)
            print(f"A placa {nova_placa} foi inserida no sistema.")
        else:
            print(f"A placa {nova_placa} já está no sistema.")

elif opcao == "2":
        consulta = input("Digite a placa para consultar: ")
        if consulta in placas:
            print(f"A placa {consulta} está no sistema.")
        else:
            print(f"A placa {consulta} não foi encontrada.")

elif opcao == "3":
        remove = input("Digite a placa para remover: ")
        if remove in placas:
            placas.remove(remove)
            print(f"A placa {remove} foi removida.")
        else:
            print(f"A placa {remove} não foi encontrada.")

elif opcao == "4":
        placas.clear()
        print("Sistema limpo com sucesso.")

elif opcao == "5":
        if placas:
            print("Placas no sistema:")
            for p in placas:
                print(p)
        else:
            print("Nenhuma placa no sistema.")

 elif opcao == "0":
        print("Saindo do sistema...")
        break

 else:
        print("Opção inválida. Tente novamente.")
