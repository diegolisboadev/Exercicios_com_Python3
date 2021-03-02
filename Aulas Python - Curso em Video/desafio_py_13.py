#====DESAFIO PYTHON 13 CV ====

preco_produto = float(input('Insira o preço do Produto R$ '))

#Com Desconto de 5%
novo_preco = preco_produto - (preco_produto*0.15) #preco_produto - (preco_produto*5/100)

print('O Produto de Preço {} com Desconto de 5% fica {:.1f}'.format(preco_produto, novo_preco))