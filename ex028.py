from random import randint
computer = randint(0,5) #Faz  o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar!')
print ('-=' * 20)
jogador = int(input('Um que número eu pensei?')) #Jogador tenta adivinhar
if jogador == computer:
    print('Parabéns!!! Você acertou!!!')
else:
    print(f'Ganhei!!! Eu pensei no número {computer} e não no número {jogador}')


