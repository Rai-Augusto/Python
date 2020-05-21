# Ex.016
from math import trunc

num = float ( input ( 'Digite um número:' ) )
print ( 'O número {} tem parte inteira igual a {}'.format ( num, trunc ( num ) ) )
print ( 'O número {} tem parte inteira igual a {}'.format ( num, int ( num ) ) )
# Ex.017
import math

co = float ( input ( 'Coloque aqui o valor do cateto oposto:' ) )
ca = float ( input ( 'Coloque aqui o valor do cateto adjacente:' ) )
hip = (co ** 2 + ca ** 2) ** (1 / 2)
print ( 'A hipotenusa é {:.1f}'.format ( hip ) )
hip = math.hypot ( co, ca )
print ( 'A hipotenusa é {:.1f}'.format ( hip ) )
# Ex.018
â = float ( input ( 'Insira aqui qual ângulo você deseja:' ) )
Seno = math.sin ( math.radians ( â ) )
Cosseno = math.cos ( math.radians ( â ) )
Tangente = math.tan ( math.radians ( â ) )
print ( 'Seno = {:.2f}'.format ( Seno ) )
print ( 'Cosseno = {:.2f}'.format ( Cosseno ) )
print ( 'Tangente = {:.2f}'.format ( Tangente ) )
# Ex.019
from random import choice

a = input ( 'Insira um nome:' )
b = input ( 'Insira um nome:' )
c = input ( 'Insira um nome:' )
d = input ( 'Insira um nome:' )
lista = [a, b, c, d]
sorteado = choice ( lista )
print ( 'O sorteado foi {} !'.format ( sorteado ) )
# Ex.020
from random import shuffle

e = input ( 'Insira um nome:' )
f = input ( 'Insira um nome:' )
g = input ( 'Insira um nome:' )
h = input ( 'Insira um nome:' )
lista2 = [e, f, g, h]
shuffle ( lista2 )
print ( 'A ordem dos fatores sorteados é {}'.format ( lista2 ) )
