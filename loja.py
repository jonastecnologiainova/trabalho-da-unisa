# Estoque inicial de produtos
produtos_disponiveis = ["blusa", "celular", "fone de ouvido"]
categorias = {
    "blusa": ("vestuário", 55, 30),
    "celular": ("eletrônico", 1555, 15),
    "fone de ouvido": ("eletrônico", 111, 25)
}

# Encomendas dos clientes
encomendas = {
    "Gabi": [
        ("blusa", "vestuário", 55, 3),
        ("celular", "eletrônico", 1555, 1),
        ("fone de ouvido", "eletrônico", 111, 1)
    ]
}

while True:
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Finalizar compra")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionarproduto = input("Digite o nome do produto a ser adicionado: ").lower()
        if adicionarproduto in categorias:
            adicionarcategoria, adicionarvalor, adicionarquantidade_max = categorias[adicionarproduto]
            adicionarquantidade = int(input("Digite a quantidade de produtos: "))
            
            if adicionarquantidade <= adicionarquantidade_max:
                p = (adicionarproduto, adicionarcategoria, adicionarvalor, adicionarquantidade)
                encomendas["Gabi"].append(p)
                categorias[adicionarproduto] = (adicionarcategoria, adicionarvalor, adicionarquantidade_max - adicionarquantidade)
                print(f"Produto '{adicionarproduto}' adicionado.")
            else:
                print("Quantidade insuficiente no estoque.")
        else:
            print("Produto não encontrado.")
        print(encomendas["Gabi"])

    elif opcao == "2":
        removerproduto = input("Digite o nome do produto a ser removido: ").lower()
        if removerproduto in categorias:
            for item in encomendas["Gabi"]:
                if item[0] == removerproduto:
                    encomendas["Gabi"].remove(item)
                    adicionarcategoria, adicionarvalor, adicionarquantidade_max = categorias[removerproduto]
                    categorias[removerproduto] = (adicionarcategoria, adicionarvalor, adicionarquantidade_max + item[3])
                    print(f"Produto '{removerproduto}' removido.")
                    break
            else:
                print("Produto não encontrado na encomenda.")
        else:
            print("Produto não encontrado.")
        print(encomendas["Gabi"])

    elif opcao == "3":
        total = sum(item[2] * item[3] for item in encomendas["Gabi"])
        print(f"Total da compra: R$ {total:.2f}")
        if total > 500:
            desconto = total * 0.10
            total -= desconto
            print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Total final: R$ {total:.2f}")
        encomendas["Gabi"].clear()
        print("Compra finalizada.")
        print("Iniciando nova venda...")

    preço = float(input('qual o preço do produto? R$'))
    novo = preço - (preço * 10/ 100)
    print ('O produto que custava R${}, na promoção com desconto de 10% vai custar R${}'.format(preço, novo))

    
   
    

