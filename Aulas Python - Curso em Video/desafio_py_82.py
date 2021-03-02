
# Exercicio 82

# Informo a expressão
expressao = list(str(input('Informe sua expressão (com parenteses): ')).strip())

# Tratar a exceção caso não informem o parenteses na setença
try:
    if expressao.index('(') != -1 and expressao.index(')') != -1:
        print('Expressão correta!' if expressao.count('(') == expressao.count(')') else 'Expressão incorreta!')
except ValueError:
    print(f'Expressão não possui parentesis!')