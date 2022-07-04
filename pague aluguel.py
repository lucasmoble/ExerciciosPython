divida = int(input())
parcela = int(input())

prestacao = 0

while  divida >0:
        prestacao+=1
        print(f'pagamento: {prestacao}')
        print(f'antes = {divida}')
        if divida >= parcela:
            divida -= parcela
        else:
            divida =0

        print(f'depois = {divida}')
        print(f'-'*5)

        
        
    
