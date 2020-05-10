# Ex.026
frase = str ( input ( 'Digite uma frase:' ) ).upper ().strip ()
print ( 'A letra A aparece {} vezes na frase'.format ( frase.count ( 'A' ) ) )
print ( 'A letra A aparece pela primeira vez na posição {}'.format ( frase.find ( 'A' ) + 1 ) )
print ( 'A letra A aparece pela última vez na posição {}'.format ( frase.rfind ( 'A' ) ) )
# Ex.027
nome = str ( input ( 'Digite seu nome completo:' ) ).strip ()
n = nome.split ()
print ( 'Seu primeiro nome é {} e seu último {} !'.format ( n[0], n[len ( n ) - 1] ) )
# Ex.028
from random import randint
from time import sleep

numero = int ( input ( 'Escolha um número entre 0 e 9: O valor escolhido foi?' ) )
maquina = randint ( 0, 9 )
print ( 'Processando...' )
sleep ( 3 )
if numero != maquina :
    print ( 'Você errou! O número que escolhi foi {}'.format ( maquina ) )
else :
    print ( 'Parabéns você acertou!' )
# Ex.029
velocidade = float ( input ( 'Qual sua velocidade atual? ' ) )
if velocidade > 80 :
    print (
        'Você está acima do limite de velocidade permitido! Você será multado imediatamente no valor de R${} ! Espero que a punição seja educativa para você! Dirija com prudência!'.format (
            (velocidade - 80) * 7 ) )
else :
    print ( 'Muito bem, você está dentro do limite de velocidade! Dirija com cuidado e boa viagem!' )
# Ex.30
num = int ( input ( 'Introduza qualquer número inteiro aqui: ' ) )
if num % 2 == 0 :
    print ( 'É par!' )
else :
    print ( 'É ímpar!' )
