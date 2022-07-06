
# Exercicio 100

def voto(ano_nascimento):
    import datetime # Escopo local de Importação

    idade = (int(datetime.datetime.today().strftime("%Y")) - int(ano_nascimento))
    match idade:
        case idade if idade >= 18 and idade < 70: 
            return 'OBRIGATÓRIO', idade
        case idade if (idade >= 16 and idade < 18) or idade >= 70:
            return 'OPCIONAL', idade
        case _ :
            return 'NEGADO', idade

ano_nascimento = int(input('Informe o Ano de Nascimento: '))
resultado, idade = voto(ano_nascimento)
print(f'Com {idade}: O Voto é {resultado} !!!')
