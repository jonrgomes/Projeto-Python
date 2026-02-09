import math
ang=float(input('Digite o angulo que deseja:'))
seno=math.sin(math.radians(ang))
print('O angulo de {} tem o seno de {:.2f}.'.format(ang,seno))
cos=math.cos(math.radians(ang))
print('O angulo de {} tem o coseno de {:.2f}.'.format(ang,cos))

