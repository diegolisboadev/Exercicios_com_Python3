
# Exercicio 95 py

def escreva(texto):
    print('~'*len(texto))
    print(f'{texto}', end='\n')
    print('~'*len(texto))

frase = input('Informe a frase: ')
escreva(frase)