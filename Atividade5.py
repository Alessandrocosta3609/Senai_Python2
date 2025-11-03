produtos = {
    "celular": 1500.00,
    "teclado": 125.98,
    "monitor": 899.90,
    "gabinete": 255.00,
    "headset": 789.90,
    "gpu": 5376.00,
    "cpu": 1890.90,
}

while True:
    consulta = input("Informe o produto (0 para sair): ").lower()
    if consulta == "0":
        break

    if consulta in produtos:
        print(f"Produto '{consulta}' custa R$ {produtos[consulta]:.2f}")
    else:
        print("Produto não encontrado!")
        cadastro = input("Deseja cadastrar esse produto? (sim/não): ").lower()
        if cadastro == "sim":
            nome_produto = consulta 
            valor_produto = float(input("Digite o valor do produto: R$ "))
            produtos[nome_produto] = valor_produto
            print(f"Produto '{nome_produto}' cadastrado com sucesso por R$ {valor_produto:.2f}!\n")

print("\n=== Lista Atualizada de Produtos ===")
for nome, preco in produtos.items():
    print(f"{nome.capitalize()} -> R$ {preco:.2f}")
