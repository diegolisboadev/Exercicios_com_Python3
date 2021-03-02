#Laço For

for c in range(6, 0, -1):#Com o -1 ele começa no sentido antihorário tirando sempre 1 (-1)
    print(c)

n = int(input('Digite um valor: '))

for num in range(n): #n+1 para mostrar até o valor escolhido pelo user
    print(num)


inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for num in range(inicio, fim+1, passo):
    print(num)

soma = 0

for som in range(4):
    nume = int(input('Digite um valor: '))
    soma += nume
    #soma = sum(nume)
print(f'O somatório de todos os valores são: {soma}')