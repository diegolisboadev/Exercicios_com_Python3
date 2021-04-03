
# Desafio 83 py

lista = []
lista_copy = []
opcao = None
while True:
    lista.append(input('Nome: '))
    lista.append(int(input('Peso: ')))
    lista_copy.append(lista[:])
    lista.clear()
    opcao = input('Deseja continuar? ')
    if opcao.lower() == 's':
        continue
    elif opcao.lower() == 'n':
        break
    else:
        print('Opção Inválida!')

# a)
print(f'Foram cadastradas {len(lista_copy)} pessoas.')

lista_peso = []
for k, l in enumerate(lista_copy):
    lista_peso.append(lista_copy[k][1])

# b)
print(f'O maior peso foi de {max(lista_peso)}kg. As pessoas mais pesadas são {[p[0] for p in lista_copy if p[1] == max(lista_peso)]}.')
# c)
print(f'O menor peso foi de {min(lista_peso)}kg. As pessoas mais leves são {[p[0] for p in lista_copy if p[1] == min(lista_peso)]}.')