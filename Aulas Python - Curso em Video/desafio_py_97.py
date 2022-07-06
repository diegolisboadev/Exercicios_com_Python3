
# Exercicio 95 py

def contador(inicio, fim, passo):
    passo = 1 if passo == 0 else passo
    for cont in range(inicio, fim - 1 if inicio > fim else fim + 1, passo if inicio < fim or passo < 0 else -passo):
        print(cont, end=' ')
    print('FIM!')

# a)
print('==================')
contador(1, 10, 1)

# b)
print('\n')
contador(10, 0, 2)

# c)
print('\n')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: ')) 
fim = int(input('Fim: ')) 
passo = int(input('Passo: ')) 
contador(inicio, fim, passo)

print('\n=================')