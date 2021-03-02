
# ====DESAFIO PYTHON 74 CV ==== #

# Ler quatro valores pelo teclado e guarda em uma tupla

valor = int(input('Informe um valor: '))
valor2 = int(input('Informe outro valor: '))
valor3 = int(input('Informe mais um valor: '))
valor4 = int(input('Informe o último valor: '))

# Metodo Guanabara
'''valores = (int(input('Informe um valor: ')), int(input('Informe outro valor: ')),
          int(input('Informe mais um valor: ')), int(input('Informe o último valor: ')))'''

tupla = (valor, valor2, valor3, valor4)

# Tupla
print(f"Você informou os números: {tupla}.")

# a) Quantas vezes apareceu o número 9
print(f'Foram encontrados {tupla.count(9)} ocorrência do número (9).')

# b) Em que posição foi digitado o primeiro valor 3
try:
    print(f'O primeiro valor 3 foi encontrado {tupla.index(3) + 1}º posição.')
except ValueError:
    print('O valor 3 não foi encontrado em nenhuma posição.')

# c) Quais foram os números pares na tupla
print('Os números pares foram: ', end='')
for t in tupla: 
    if t % 2 == 0: print(f'{t}', end=' ')
