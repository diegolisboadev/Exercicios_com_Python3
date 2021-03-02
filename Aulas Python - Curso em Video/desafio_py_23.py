#====DESAFIO PYTHON 23 CV ====

#Mostrar se o nome da cidade começa com a palavra 'SANTO'

cidade = str(input('Insira o nome da cidade: ')).strip()

#city = cidade.split()

#if 'Santo' in city[0] or 'santo' in city[0] or 'SANTO' in city[0]:
#    print('Sua cidade começa com Santo')

#else:
#    print('Sua cidade não começa com santo!!!')

#Outro modo mais simples

print(cidade[:5].upper() == 'SANTO' or cidade[:5].upper() == 'SANTA')