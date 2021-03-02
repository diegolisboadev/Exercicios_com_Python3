#====DESAFIO PYTHON 35 CV ====

#Programa para aprovar um emprestimo bancário para comprar uma casa
#Calcule o valor da prestação mensal, sabendo que o valor não pode
#ultrapassar 30% do salário

val_casa = float(input('Qual o valor da casa? '))
sal_comprador = float(input('Qual o seu salário? '))
anos_pagar = int(input('Em quantos anos você quer pagar? '))

val_prestacao = val_casa / (anos_pagar * 12)

minimo_sal = sal_comprador * 0.3

if val_prestacao > minimo_sal:
    print('Desculpe, emprestimo negado!! O valor da prestação exceder o permitido para seu salário!!')

elif val_prestacao <= minimo_sal:
    print('Emprestimo concedido!! Obrigado por aderir ao nosso banco!!')

print('Obrigado por usar nossos serviços, Volte Sempre!!!')




