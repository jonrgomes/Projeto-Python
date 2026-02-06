fun=float(input('Qual é o valor so salário? R$'))
aum=fun+(fun*15/100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2F}'.format(fun,aum))


