
# Exercicio 103

def leiaInt(intInput):
    while intInput:
        num = input(intInput)
        if num.isnumeric() == False: 
            print('\033[0;31mERRO! Digite um  inteiro válido.\033[m')
            continue
        break
    return int(num)

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
    
   


