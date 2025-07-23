livros = []
usuarios = []

emprestimos = [] 

def menu():
    print(" --- Biblioteca --- ")
    print(" 1 - Cadastrar Livro")
    print(" 2 - Consultar Livro")
    print(" 3 - Remover Livro")
    print(" 4 - Cadastrar Usuário")
    print(" 5 - Listar Sistema")
    print(" 6 - Emprestar Livro")
    print(" 7 - Devolver Livro")
    print(" 0 - Sair")
  


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ").strip()
        livros.append({"titulo": titulo, "disponivel": True})
        print(f"O livro '{titulo}' foi cadastrado com sucesso.")

    elif opcao == "2":
        consulta = input("Digite o título do livro para consultar: ").strip()
        encontrado = False
        for livro in livros:
            if livro["titulo"].lower() == consulta.lower():
                status = "Disponível" if livro["disponivel"] else "Emprestado"
                print(f"O livro '{livro['titulo']}' está no sistema. Status: {status}")
                encontrado = True
        if not encontrado:
            print(f"O livro '{consulta}' não foi encontrado.")

    elif opcao == "3":
        remover = input("Digite o título do livro a ser removido: ").strip()
        for livro in livros:
            if livro["titulo"].lower() == remover.lower():
                livros.remove(livro)
                print(f"O livro '{remover}' foi removido.")
                break
        else:
            print(f"O livro '{remover}' não foi encontrado.")

    elif opcao == "4":
        nome_usuario = input("Digite o nome do usuário para cadastro: ").strip()
        if nome_usuario in usuarios:
            print("Usuário já cadastrado.")
        else:
            usuarios.append(nome_usuario)
            print(f"Usuário '{nome_usuario}' cadastrado com sucesso.")

    elif opcao == "5":
        if not livros:
            print("Nenhum livro na biblioteca.")
        else:
            print("\nLivros na Biblioteca:")
            for livro in livros:
                status = "Disponível" if livro["disponivel"] else "Emprestado"
                print(f"- {livro['titulo']} ({status})")

        if not usuarios:
            print("\nNenhum usuário cadastrado.")
        else:
            print("\nUsuários Cadastrados:")
            for user in usuarios:
                print(f"- {user}")

        if not emprestimos:
            print("\nNenhum livro emprestado.")
        else:
            print("\nEmpréstimos Ativos:")
            for e in emprestimos:
                print(f"- Livro: '{e['livro']}' emprestado por: {e['usuario']}")

    elif opcao == "6":
        nome_usuario = input("Digite o nome do usuário: ").strip()
        if nome_usuario not in usuarios:
            print("Usuário não cadastrado.")
            continue

        titulo_livro = input("Digite o título do livro para empréstimo: ").strip()
        for livro in livros:
            if livro["titulo"].lower() == titulo_livro.lower():
                if livro["disponivel"]:
                    livro["disponivel"] = False
                    emprestimos.append({"usuario": nome_usuario, "livro": livro["titulo"]})
                    print(f"Livro '{livro['titulo']}' emprestado com sucesso para {nome_usuario}.")
                else:
                    print(f"O livro '{livro['titulo']}' já está emprestado.")
                break
        else:
            print(f"O livro '{titulo_livro}' não foi encontrado.")

    elif opcao == "7":
        nome_usuario = input("Digite o nome do usuário que está devolvendo: ").strip()
        titulo_livro = input("Digite o título do livro que está sendo devolvido: ").strip()

        for emprestimo in emprestimos:
            if (emprestimo["usuario"] == nome_usuario and
                emprestimo["livro"].lower() == titulo_livro.lower()):
                for livro in livros:
                    if livro["titulo"].lower() == titulo_livro.lower():
                        livro["disponivel"] = True
                        emprestimos.remove(emprestimo)
                        print(f"Livro '{livro['titulo']}' devolvido com sucesso.")
                        break
                break
        else:
            print("Empréstimo não encontrado ou dados incorretos.")

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
