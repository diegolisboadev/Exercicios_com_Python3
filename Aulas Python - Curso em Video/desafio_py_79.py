
# Exercicio 79

# TODO revisar

valores = []
cont = 0

for k, v in enumerate(range(5)):
    val = int(input(f'Informe os Valores ({k}): '))
    valores.append(val)

    for i, v in enumerate(valores):
        print(f'{i} - {v}')
        if v > val:
            valores.insert((v.index(i) + 1), val)
