
# ====DESAFIO PYTHON 75 CV ==== #

# Tabela de Preços Formatados

produtos = ('bola', 10.00, 'peixe', 24.90, 'papel', 55.00, 'pano', 3.10)
# produtos_dict = {'bola': 10.00, 'peixe': 24.90, 'papel': 55.00, 'pano': 3.10}

print("-"*50)
print('LISTAGEM DE PREÇOS'.center(50))
print('-'*50)

for p in produtos:
    if type(p) == str:
        prod = p
        produto = f'{prod:.<30} R$ '
    else:
        pre = p
        resultado = f"{produto}{pre}"
        print(f'{resultado}')

print('-'*50)

# Solução Guanabara
'''for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>5.2f}')'''