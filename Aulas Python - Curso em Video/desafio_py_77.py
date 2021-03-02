
# Exercicio 77

def lista_max(lista):
    max_item = max(lista)
    max_lista = []
    for pos, l in enumerate(lista):
        if max_item == l:
            max_lista.append(pos)
    return max_lista

def lista_min(lista):
    min_item = min(lista)
    min_lista = []
    for pos, l in enumerate(lista):
        if min_item == l:
            min_lista.append(pos)
    return min_lista

lista = []
for key, valor in enumerate(range(5)):
    lista.append(int(input(f'Digite um Valor ({key}): ')))

print("=" * 30)
print(f'O valores digitados foram {lista}', end='\n')

max_lista = lista_max(lista)
min_lista = lista_min(lista)

# Maior valor da lista
maior = [ma for ma in max_lista]
print(f'O maior valor da lista é {max(lista)} e foi encontrado nas posições {str(maior)}', end='\n')

# Menor valor da lista
menor = [mi for mi in min_lista]
print(f'O menor valor da lista é {min(lista)} e foi encontrado nas posições {str(menor)}', end='\n')