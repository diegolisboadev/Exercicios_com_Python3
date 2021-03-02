
#====DESAFIO PYTHON 15 CV ====

#Preço a pagar pelo o uso de carro alugado sabendo os KM e os dias Alugados

dias_alug = int(input('Dias Alugado: '))
km_rodados = float(input('Km Rodados: '))

preco_pagar = (dias_alug*60) + (km_rodados*0.15)

print('O veiculo foi alugado por {} dias e percorreu {} Km, o preço a pagar'
      'pelo aluguel é de R$ {:.2f}'.format(dias_alug, km_rodados, preco_pagar))
