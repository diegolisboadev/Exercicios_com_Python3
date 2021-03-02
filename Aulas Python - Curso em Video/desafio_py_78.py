
# Exercicio 78

num_lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in num_lista:
        num_lista.append(num)
    else:
        print('Valor já informado!!')

    op = input('Que continuar? [S/N]').upper()
    if op == 'N':
        break

print('+='*30)
print(f'Todos os número digitados foram {sorted(num_lista)}')