
#====DESAFIO PYTHON 60 CV ====

#Ler o primeiro termo e razão e mostra os 10 primeiros valores da PA com WHILE

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

formula = (primeiro_termo + (9 * razao) + razao)

while primeiro_termo < formula:
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao

print('FIM')