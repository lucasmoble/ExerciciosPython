km_perc=float(input('Quantos KM você percorreu? '))
dias_alugado=int(input('Quantos dias você ficou com ele? '))

dias = dias_alugado * 60
km_rodado = km_perc *0.15

total = dias + km_rodado

print('o total a ser pago é {:.2f}'.format(total))
