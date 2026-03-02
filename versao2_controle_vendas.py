# versao2_controle_vendas.py

vendas = []

def registrar_venda():
    cliente = input("Nome do cliente: ")
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(input("Valor unitário: "))
    
    total = quantidade * valor_unitario
    
    vendas.append({
        "cliente": cliente,
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "total": total
    })
    
    print("Venda registrada com sucesso!")

def total_geral():
    if not vendas:
        print("Nenhuma venda registrada.")
        return
    
    total = sum(v["total"] for v in vendas)
    print(f"Total vendido: R$ {total:.2f}")

def cliente_campeao():
    if not vendas:
        print("Nenhuma venda registrada.")
        return
    
    ranking = {}
    
    for v in vendas:
        cliente = v["cliente"]
        ranking[cliente] = ranking.get(cliente, 0) + v["total"]
    
    campeao = max(ranking, key=ranking.get)
    
    print(f"\nCliente campeão: {campeao}")
    print(f"Total comprado: R$ {ranking[campeao]:.2f}")

def menu():
    while True:
        print("\n=== SISTEMA DE VENDAS V2 ===")
        print("1 - Registrar venda")
        print("2 - Mostrar total geral")
        print("3 - Mostrar cliente campeão")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_venda()
        elif opcao == "2":
            total_geral()
        elif opcao == "3":
            cliente_campeao()
        elif opcao == "4":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
