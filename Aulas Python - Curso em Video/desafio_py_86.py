
# Desafio 86

matriz = [[], [], []]
soma_pares = soma_terceira_coluna = maior_valor_segunda_linha = 0
for k, m in enumerate(matriz):
    for l in range(3):
        matriz[k].append(int(input(f'Posição {[k, l]} Informe um valor: ')))

print('=-='*30)
for k, m in enumerate(matriz):
    for l in matriz[k]:
        print(f'[ {l} ]', end=' ')

        if l % 2 == 0:
            soma_pares += l

    soma_terceira_coluna += matriz[k][2]
    maior_valor_segunda_linha = max(matriz[1])
    print('\n')
print('=-='*30)

# a) A SOMA DE TODOS OS VALORES DIGITADOS
print(f'A Soma de todos os valores digitados e [{soma_pares}]')

# b) A SOMA DOS VALORES DA TERCEIRA COLUNA
print(f'A Soma dos valores da 3 coluna é [{soma_terceira_coluna}]')

# c) O MAIOR VALOR DA SEGUNDA LINHA
print(f'O maior valor da segunda linha é [{maior_valor_segunda_linha}]')