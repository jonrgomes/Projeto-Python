#Peça um nome e digite uma mensagem personalizada.
nome = input('Qual o seu nome?').strip()
print(f'Prazer em te conhecer {nome}!')
#Peça dois numeros interios e a soma deles!
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
s=n1+n2
print(f'A soma de {n1} + {n2} é {s}!')
#Receba 3 notas e calcule a média aritimética!
print('Diigite as notas do aluno:')
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceita nota:'))
m=(n1+n2+n3)/3
print(f'A média final obtida é: {m:.2f}')
#Converta a temperatura de Cº para Fº:
c = float(input('Digite um temperatura em Cº:'))
print('Quanto vale essa temperatura em Fº?')
tf = (c*1.8)+32
print(f'Em Fº essa temperatura vale {tf:.0f}!')
#Peça um número e diga se ele é par ou impar!
num = int(input('Digite um número:'))
if num % 2 == 0:
    print('Este número é par!')
else:
    print('Este numero é impar!')
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 10:
    print('Carro seminovo em!!!')
else:
    print('Seu carro está velho')



