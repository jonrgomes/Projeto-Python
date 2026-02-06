preço=float(input('Qual o preço do poduto? R$'))
desconto=preço-(preço*5/100)
print('Aplicando o desconto de 5% temos o valor de R${:.2f}!'.format(desconto))
