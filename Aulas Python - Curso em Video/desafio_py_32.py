#====DESAFIO PYTHON 31 CV ====

#Verificar o menor e o maior valor entre 3 números

nums = []

for num in range(0,3):
    valor = int(input('Informe um número: '))
    nums.append(valor)

print('O Maior número é {}'.format(max(nums)))
print('O menor número é {}'.format(min(nums)))
