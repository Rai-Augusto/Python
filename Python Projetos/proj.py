print ( 'Olá seja bem vindo!' )
nome = input ( 'Qual seu nome?' )
print ( "{} tenho um desafio para você".format ( nome ) )

import time
time.sleep(2)
print ( 'O Desafio:' )
time.sleep(2)
print ( 'É somar o quadrado de quatro números primos consecutivos e acertar a soma.' )
time.sleep(2)
print ( 'Você está preparado?' )
time.sleep(2)

print ( 'Exemplo:' )
time.sleep(2)
print ( 'n1=17' )
time.sleep(2)
print ( 'n2=19' )
time.sleep(2)
print ( 'n3=23' )
time.sleep(2)
print ( 'n4=29' )
time.sleep(2)
print ( 'n= 2020' )

time.sleep(5)

print ( 'Insira aqui suas apostas para nosso Desafio' )

inicio = 1
contar_divisores = 0

N1 = int ( input ( 'N1:' ) )
while inicio <= N1 :
    if N1 % inicio == 0 :
        contar_divisores = contar_divisores + 1
    inicio = inicio + 1
    if contar_divisores > 2 :
        print ( 'Não é primo!' )
        break

inicio1 = 1
contar_divisores1 = 0

N2 = int ( input ( 'N2:' ) )
while inicio1 <= N2 :
    if N2 % inicio1 == 0 :
        contar_divisores1 = contar_divisores1 + 1
    inicio1 = inicio1 + 1
    if contar_divisores1 > 2 :
        print ( 'Não é primo!' )
    if not N2 > N1 :
        print ( 'Não é consecutivo!' )
        break

inicio2 = 1
contar_divisores2 = 0

N3 = int ( input ( 'N3:' ) )
while inicio2 <= N3 :
    if N3 % inicio2 == 0 :
        contar_divisores2 = contar_divisores2 + 1
    inicio2 = inicio2 + 1
    if contar_divisores2 > 2 :
        print ( 'Não é primo!' )
    if not N3 > N2 :
        print ( 'Não é consecutivo!' )
        break

inicio3 = 1
contar_divisores3 = 0

N4 = int ( input ( 'N4:' ) )
while inicio3 <= N4 :
    if N4 % inicio3 == 0 :
        contar_divisores3 = contar_divisores3 + 1
    inicio3 = inicio3 + 1
    if contar_divisores3 > 2 :
        print ( 'Não é primo!' )
    if not N4 > N3 :
        print ( 'Não é consecutivo' )
        break

N = N1 ** 2 + N2 ** 2 + N3 ** 2 + N4 ** 2

Ns = int ( input ( 'A sua soma é:' ) )

if Ns != N :
    print ( 'Que pena,você perdeu!' )
while Ns == N :
    if contar_divisores > 2 :
        print ( 'Que pena,você perdeu!' )
    if contar_divisores1 > 2 :
        print ( 'Que pena,você perdeu!' )
    if not N2 > N1 :
        print ( 'Que pena,você perdeu!' )
    if contar_divisores2 > 2 :
        print ( 'Que pena,você perdeu!' )
    if not N3 > N2 :
        print ( 'Que pena,você perdeu!' )
    if contar_divisores3 > 2 :
        print ( 'Que pena,você perdeu!' )
    if not N4 > N3 :
        print ( 'Que pena,você perdeu!' )
    else :
        print ( 'Parabéns, você ganhou! ' )
        break

