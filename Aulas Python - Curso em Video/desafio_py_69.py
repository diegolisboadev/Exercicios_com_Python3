
# ====DESAFIO PYTHON 69 CV ====

#ESTOQUE BÁSICO

print("---"*30)
print("--- LOJA CV ---")
print("---"*30)

preco_maior_1000 = total = preco_menor = cont = 0
prod_barato = None

while True:

    nome = input("Informe o nome do Produto: ")
    preco = int(input("Informe o preço do Produto: "))
    cont += 1

    opcao = input("Deseja cadastrar mais informações [S/N]: ").upper().strip()[0]

    # calcular o total do carrinho
    total += preco

    # PRECO MAIOR QUE 1000
    if preco > 1000:
        preco_maior_1000 += 1

    # PRODUTO MAIS BARATO
    if cont == 1 or preco < preco_menor:
        preco_menor = preco
        prod_barato = nome

    if opcao == "N":
        print("---FINALIZAÇÃO DO PROGRAMA---")
        print(f"Total de Gasto na Compra (Carrinho) foi R$ {total:.2f}: ")
        print(f"Existem {preco_maior_1000} produtos com o preco maior que R$ 1000.")
        print(f"O produto mais barato é {prod_barato} de valor R$ {preco_menor:.2f}")
        break