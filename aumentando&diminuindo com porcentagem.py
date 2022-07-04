salario_atual=float(input())

aumento = salario_atual +(salario_atual * 15/100)
desconto = salario_atual -(salario_atual * 15/100)
print('Seu salário antigo era {:.2f} e o seu novo salário passa a ser {:.2f}'.format(salario_atual,aumento))
print('Seu salário antigo era {:.2f} e o seu novo c/ desconto é {:.2f}'.format(salario_atual,desconto))
