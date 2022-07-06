
# Interactive Help
help('max')
print(input,__doc__)

def teste():
    """
        -> Teste docstring
        return: sem retorno
    """
    print('p')

help(teste)

# Argumentos 
def somar(a,b,c=0):
    print(a+b+c)

# Nomeados 
somar(c=1, b=2, a=2)

# Opcionais
somar(2, 2)
