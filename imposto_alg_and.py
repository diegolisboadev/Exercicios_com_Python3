
#Cálculo do Imposto com and, or ou not

imposto = float(input('Imposto? '))

if imposto < 10 :
    print('Baixo')
    
elif imposto >= 10 and imposto <= 27 :
    print('Médio')

elif imposto > 27 and imposto < 100 :
    print('Alto')

else:
    print('Imposto Inválido')

print('Obrigado por utilizar o Programa!!')
