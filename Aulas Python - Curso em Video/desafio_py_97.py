
# Exercicio 95 py
# TODO

def contador(inicio, fim, passo):
    for cont in range(inicio, fim, -passo if inicio > fim else passo):
        print(cont, end=' ')

# a)
print('==================')
contador(1, 10, 1)

# b)
print('\n')
contador(10, 0, 2)

# c)
print('\n')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio ')) 
fim = int(input('Fim ')) 
passo = int(input('Passo ')) 
contador(inicio, fim, passo)

print('\n=================')