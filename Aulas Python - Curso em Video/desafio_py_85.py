
# Desafio 85

matriz = [[], [], []]
for k, m in enumerate(matriz):
    for l in range(3):
        matriz[k].append(int(input(f'Posição {[k, l]} Informe um valor: ')))

print('=-='*30)
for k, m in enumerate(matriz):
    for l in matriz[k]:
        print(f'[ {l} ]', end=' ')
    print('\n')