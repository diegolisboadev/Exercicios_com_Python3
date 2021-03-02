# Iniciando desafio 2

#Pegando e imprimindo a data de nascimento atraves de um
#usando if para questionar se a data está correta ou não

print('====DESAFIO 2=====')

#dia = input('Dia? ')
#mes = input('Mês? ')
#ano = input('Ano? ')

# print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto? (y|n)')



# Função para verificação

def dataNasc():

    dataNasc = input('Informe a sua data de nascimento. ex(00/00/0000)')

    print('Você nasceu no dia {0}'.format(dataNasc))

    result = input('A data está correta? (s|n) ')

    return result


# Função main
def main():
    if dataNasc() != 's':
        print('Tente Novamente!!')
        dataNasc()
    else:
        print('Obrigado!!!')
        exit(-1)



# Chamada da função main()
if __name__ == '__main__':
    main()
