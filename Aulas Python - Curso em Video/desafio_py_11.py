#====DESAFIO PYTHON 11 CV ====
#Crie um programa que leia quanto de dinheiro
#uma pessoa tem na carteira e mostre quantos dolares ela
#pode comprar
#considere: USS 1 dolar = R$ 3,27

#Verificando quando de reais posso comprar em dolares

carteira = float(input('Dinheiro na Carteira R$? '))

dolar = (carteira/3.27)
#euro =

print('Dolares comprados: US$ {:.2f}'.format(dolar))
