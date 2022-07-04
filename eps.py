lista_de_dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

def verifica_dia_entrada(entrada, lista):
    
    if entrada in lista:
        return True
    else:
        return False

def verifica_quant_de_dias(dias):
    
    if dias > 6 or dias < 0:
        return False
    else:
        return True 

diaDaSemana = False

while(not dia_da_semana):
    dia_entrada = input('Digite o dia da semana: ')
    dia_da_semana = verifica_dia_entrada(dia_entrada, lista_de_dias)
    
prazoDeEspera = False

while(not prazo_de_espera):
    quant_dias = int(input('Quantidade de dias da entrega: '))
    prazo_de_espera = verifica_quantde_dias(quant_dias)
    

if quant_dias == 0:
    print('Seu Pedido CHega Hoje!')
else:
    indexDoDiaSemana = listaDeDias.index(diaEntrada)
    novaLista = listaDeDias[indexDoDia_aemana + 1:len(lista_de_dias)] + lista_de_dias[0:indexDoDiaSemana]

    diaEntrega = novaLista[quantDias - 1]

    print('Será entregue dia ', diaEntrega)

