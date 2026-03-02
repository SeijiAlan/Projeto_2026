def menu():
    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Listar vendas")
    print("3 - Mostrar total vendido")
    print("4 - Sair")


vendas = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente = input("Nome do cliente: ")
        produto = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: "))

        total = quantidade * valor_unitario

        venda = {
            "cliente": cliente,
            "produto": produto,
            "quantidade": quantidade,
            "valor_unitario": valor_unitario,
            "total": total
        }

        vendas.append(venda)
        print("Venda registrada com sucesso!")

    elif opcao == "2":
        for v in vendas:
            print(v)

    elif opcao == "3":
        total_geral = sum(v["total"] for v in vendas)
        print(f"Total vendido: R$ {total_geral:.2f}")

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")

menu()