#====DESAFIO PYTHON 14.2 CV ====

#Pagamento com 10% de desconto à vista e 8% de desconto a prazo

preco_produto = float(input('Informe o preço do produto: '))

pagamento = input('Informe o tipo de pagamento (se á vista digite Vista se à prazo digite Prazo '
                  'ou (0) para sair. ')

if pagamento.lower() == 'vista' or pagamento.title() == 'Vista' or pagamento.upper() == 'VISTA':

    print('0 produto de valor {}, com desconto à vista custa {}'.
          format(preco_produto, (preco_produto - (preco_produto * 0.1))))
    print('Obrigado e volte sempre!!!')

elif pagamento.lower() == 'prazo' or pagamento.title() == 'Prazo' or pagamento.upper() == 'PRAZO':
    print('0 produto de valor {}, com desconto à prazo custa {}'.
          format(preco_produto, (preco_produto - (preco_produto * 0.08))))
    print('Obrigado e volte sempre!!!')

else:
    print('Obrigado por visitar nossa loja!!! Volte sempre!!!')
