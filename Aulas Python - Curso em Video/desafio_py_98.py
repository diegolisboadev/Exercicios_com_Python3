
# Exercicio 95 py

def maior(*inteiros):
    inteiros = 0 if inteiros == 0 else inteiros
    print(f'Analisando os valores {[val for val in inteiros]}')
    print(f'Foram informados {len(inteiros)} ao todo.')
    return max(inteiros)

def resultadoPrint(valor):
    print(f'O maior valor informado foi {valor}', end='\n')
    print('-=-'*20)

resultadoPrint(maior(2,9,4,5,7,1))
resultadoPrint(maior(4,7,0))
resultadoPrint(maior(1,2))
resultadoPrint(maior(6))
resultadoPrint(maior(0))
