print('Olá, Mundo!')
nome=input('Digite seu nome:')
print('Prazer em te conhecer,{}!'.format(nome))
n=int(input('Digite um valor:'))
o=int(input('Digite outro valor:'))
p=n/o
print('A divisão é {:.2f}!'.format(p))
print('O tipo primitivo deste valor é:',type(p))
print('É numérico?')
print(str(p).isnumeric())
print('É alfanumérico?')
print(str(p).isalpha())
print('Contem espaços?')
print(str(p).isspace())
a=int(input('Digite um valor e terá o antecessor e o sucessor:'))
d=a-1
e=a+1
print('Sabe-se que o antecessor é {} e o sucessor é {} para o número {}'.format(d,e,a))











