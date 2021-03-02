num = [2,5,9,1]
num[2] = 3
num.append(7)

# Aula Aprendendo sobre Listas em Python
num.sort(reverse=True)
num.insert(2, 0)
# num.pop(2)
# num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)}')

# Parte 2
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(5):
    # valores.append(int(input('Digite um valor: ')))
    pass

for key, v in enumerate(valores):
    # print(f'{v}...', end='')
    print(f'Na posição {key}, encontrei {v}')

a = [2,3,4,7]
b = a[:] # B recebe copia de A
b[2] = 8
print(a)
print(b)