
#====DESAFIO PYTHON 54 CV ====

#Ler o peso de 5 pessoas e dizer qual o maior e o menor peso

peso_add = []

for p in range(6):#6
    peso = float(input('Informe seu peso: '))
    peso_add.append(peso)

print('O maior peso lido é {}Kg'.format(max(peso_add)))
print('O menor peso lido é {}Kg'.format(min(peso_add)))