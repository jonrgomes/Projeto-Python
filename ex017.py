cop=float(input('Comprimento do cateto oposto:'))
adj=float(input('Comprimento do cateto adjacente:'))
hip=(cop**2+adj**2)**(1/2)
print('A hipotenusa mede {:.2f}.'.format(hip))
#OU
import math
co=float(input('Comprimento do cateto oposto:'))
ad=float(input('Comprimento do cateto adjacente:'))
hi=math.hypot(co,ad)
print('Assi a hipotenusa mede {:.2f}.'.format(hip))
