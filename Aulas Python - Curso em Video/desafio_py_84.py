
# Desafio 84 py

numeros = [[], []]
for n in range(1,8):
    num = int(input(f'{n} - Informe um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares são: {numeros[0]}')
print(f'Os valores impares são: {numeros[1]}')