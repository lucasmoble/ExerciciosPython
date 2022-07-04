# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:, formúla matematica
# para solucionar o problema!


inicio = int(input())
fim = int(input())

count = 0

for ano in range(inicio, fim + 1):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano)
        count += 1
      
print('bissextos: {}'.format(count))
