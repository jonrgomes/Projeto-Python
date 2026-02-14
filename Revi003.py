#Peça um nome e digite uma mensagem personalizada.
nome = input('Qual o seu nome?').strip()
print(f'Prazer em te conhecer {nome}!')
#Peça dois numeros interios e a soma deles!
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
s=n1+n2
print(f'A soma de {n1} + {n2} é {s}!')
#Receba 3 notas e calcule a média aritimética!
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceita nota:'))
m=(n1+n2+n3)/3
print(f'A média final obtida é: {m:.2f}')

