
# Exercicio 80

lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    op = input('Deseja continuar? [S/N]').upper()
    if op == 'N':
        break

# Quanto números foram digitados
print(f'Foram digitados {len(lista)} números!')

# Valores de forma decrescente
print(f'Lista de forma descrescente {sorted(lista, reverse=True)}!')

# Se o valor 5 foi digitado e está ou não na lista
if 5 in lista:
    print(f'O valor 5 está na lista e encontra-se na {lista.index(5)}º posição!')
else:
    print('O valor 5 não está na lista!')