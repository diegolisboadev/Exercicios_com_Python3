
#====DESAFIO PYTHON 43 CV ====

#Calcula o valor a ser pago por um produto

print('{:=^40}'.format(' Lojas Mustella '))
print('{:=^40}'.format(' Seja Bem Vindo (a) '))

preco_produto = float(input('Informe o preço do produto R$: '))
print('Informe a condição de pagamento, informando abaixo o valor referente a condição de pagamento:\n'
'1 - Á vista DINHEIRO / CHEQUE: 10 % de desconto \n'
'2 - Á vista NO CARTAO: 5% de desconto \n'
'3 - Até 2X no CARTÃO: Preço normal \n'
'4 - 3x ou mais no CARTÃO: 20% de juros')

cond_pagamento = int(input('Escolha a forma e digite o número referente a condição: '))

resultado = 0

if cond_pagamento == 1:
    resultado = preco_produto - (preco_produto * 0.1)

elif cond_pagamento == 2:
    resultado = preco_produto - (preco_produto * 0.05)

elif cond_pagamento == 3:
    resultado = preco_produto
    parcela = resultado / 2
    print('Sua compra será parcelada em 2x de R${} no CARTÃO'.format(parcela))

elif cond_pagamento == 4:
    parcela = int(input('Quantas parcelas: '))
    resultado = preco_produto + (preco_produto * 0.2)
    print('Sua compra será parcelada em {}x de R${} com JUROS'.format(parcela, (resultado / parcela)))
else:
    print('Ops!! Valor condição de pagamento inexistente! Tente novamente!')

print('Sua compra de R$ {}, vai custar R$ {} no final!!'.format(preco_produto, resultado))

print('Obrigado pela sua compra!! Volte sempre!!')