#====DESAFIO PYTHON 38 CV ====

#Ler o ano de nascimento e informa se já está ou nao pronto para se alistar

from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))
sexo = input('Qual o seu sexo: ').strip().lower()

ano_atual = date.today().year

idade = ano_atual - ano_nasc

ano_apres = ano_nasc + (idade - 18) * -1

ano_to_apres = ano_atual - (idade - 18)

if sexo == 'f':
    print('Desculpe você não pode se alistar!!!')

elif idade < 18 and sexo == 'm':
    print('Você tem {} anos, por isso ainda irá se alistar no serviço militar!!'.format(idade))
    print('Faltam {} anos para você se alistar'.format((idade - 18) * -1))
    print('Você deve se apresentar no ano de {}'.format(ano_apres))
elif idade == 18 and sexo == 'm':
    print('Você tem {} ano e deve se apresentar a uma junta militar!!'.format(idade))
    print('Corra logo para você se alistar')
elif idade > 18 and sexo == 'm':
    print('Você tem {} anos e já passou do tempo de se apresentar ao serviço militar!!'.format(idade))
    print('Passou {} anos do prazo para se apresentar na juntar militar'.format(idade - 18))
    print('Você deveria se apresentar no ano de {}'.format(ano_to_apres))
elif sexo != 'm' or sexo != 'f':
    print('Sexo inválido!!')