dist = float(input('Qual a distancia da viagem?'))
print(f'Você está prestes a começar uma viagem de {dist}km!')
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print(f'E o preço da sua passagem será de {preço} reais!')