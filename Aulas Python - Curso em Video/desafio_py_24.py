#====DESAFIO PYTHON 24 CV ====

#Pega o nome da pessoa e dizer se ela tem 'SILVA' no nome

nome = str(input('Insira seu nome: ')).strip()

#if 'SILVA' in nome or 'silva' in nome or 'Silva' in nome:
    #print('Tem Silva no Nome!!')

#else:
    #print('Não tem Silva no Nome!!!')

#Outro modo mais simples
print('Seu nome tem Silva {}'.format('SILVA' in nome.upper()))