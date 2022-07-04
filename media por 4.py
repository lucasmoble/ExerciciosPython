n1, n2, n3, n4 = int(input("")).split()

media = float(n1 + n2 + n3 + n4)/4

if media >= 7.0:
    print("aluno aprovado")
    
elif media < 5.0:
        print ("aluno reprovado")
