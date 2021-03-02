
# Exercicio 81

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))

    op = input('Deseja continuar? [S/N]').upper()
    if op == 'N':
        break

# Lista somente com valores pares ou impares
for l in lista:
    if l % 2 == 0:
        pares.append(l)
    else:
        impares.append(l)

print('-='*30)

# Printando as listas
print(f'Lista geral {lista}', end='\n')
print(f'Lista de pares {pares}', end='\n')
print(f'Lista de impares {impares}', end='\n')
        