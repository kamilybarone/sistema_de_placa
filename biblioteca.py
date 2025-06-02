
while True:
    print("--- SISTEMA DE PLACAS ---")
    print("1 -  Adicionar Placas   ")
    print("2 -  Consultar Placas   ")
    print("3 -  Remover Placas   ")
    print("4 -  Limpar Sistema   ")
    print("5 -  Listar Sistema   ")
    print("0 -  Sair   ")

    opção = input("Escolha uma opção: ")

    if opção == "1":
        placa = input("Digite a placa para adicionar: ")
        if placa not in placa:
            placa.append(placa)
            print(f"A placa {placa} foi inserida no sistema.")
        else:
            print(f"A placa {placa} já está no sitema")

    elif opção == "2":
        consulta = input("Digite a placa para consultar: ") placa = []
        if consulta in placa:
            print(f"A placa {consulta} está no sistema.")
        else:
            print(f"A placa {consulta} não foi encontrada.")

    elif opção == "3":
        remove = input("Digite a placa para remover: ")
        if remove in placa:
            placa.remove(remove)
            print(f"A placa {remove} foi removida.")
        else:
            print(f"A placa {remove} não foi encontrada.")

    elif opção == "4":
        placa.clear() 
        print("Sistema limpo com sucesso.")

    elif opção == "5":
        print("Placas no sistema:")
        for placa in placa:
            print(placa)

    elif opção == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        
