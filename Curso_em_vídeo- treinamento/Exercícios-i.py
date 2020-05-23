# Ex.041
from datetime import date

ano = int ( input ( 'Qual o ano que você nasceu?' ) )
cat = date.today ().year - ano
if cat <= 9 :
    print ( 'Categoria Mirim' )
elif 10 <= cat <= 14 :
    print ( 'Categoria Infantil' )
elif 14 <= cat <= 19 :
    print ( 'Categoria Junior' )
elif 19 <= cat <= 25 :
    print ( 'Categoria Sênior' )
else :
    print ( 'Categoria Master' )

# Ex.042
print ( 'Vamos analisar trinagulos, digite três lados' )
l1 = float ( input ( 'Digite um lado: ' ) )
l2 = float ( input ( 'Digite um lado: ' ) )
l3 = float ( input ( 'Digite um lado: ' ) )
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 :
    print ( 'Os lados adicionados podem formar triângulos!' )
    if l1 == l2 and l1 == l3 and l2 == l3 :
        print ( 'O triângulo é equilatero !' )
    elif l1 == l2 or l1 == l3 or l2 == l3 :
        print ( 'O triângulo é isoceles !' )
    else :
        print ( 'Triângulo escaleno !' )
else :
    print ( 'Os lados adicionados não podem formar triângulos! Tente Outra vez !' )

# Ex.043
print ( 'Vamos calcular seu IMC!' )
massa = float ( input ( 'Massa: ' ) )
altura = float ( input ( 'Altura: ' ) )
imc = massa / (altura ** 2)
print ( 'Seu IMC foi de {:.2f}'.format ( imc ) )
if imc <= 18.5 :
    print ( 'Abaixo do peso!' )
elif 18.5 < imc <= 25 :
    print ( 'Peso ideal !' )
elif 25 < imc <= 30 :
    print ( 'Sobrepeso !' )
elif 30 < imc <= 40 :
    print ( 'Obesidade !' )
else :
    print ( 'Obesidade mórbida !' )

# Ex.044
print ( '{:=^40}'.format ( 'Bem vindo a minha loja ! ' ) )
din = float ( input ( 'Qual o valor dos produtos comprados? R$ ' ) )
print ( '''Formas de pagamento:
[1] Dinheiro/Cheque
[2] A vista no cartão
[3] 2x no cartão
[4] 3x no cartão''' )
dinf = int ( input ( 'Qual a forma de pagamento ? Digite aqui o número : ' ) )
if dinf == 1 :
    print ( 'O valor de R$ {:.2f} selecionando a opção de pagamento 1, o valor passa a ser R$ {:.2f}'.format ( din,
                                                                                                               din * 0.9 ) )
elif dinf == 2 :
    print ( 'O valor de R$ {:.2f} selecionando a opção de pagamento 2, o valor passa a ser R$ {:.2f}'.format ( din,
                                                                                                               din * 0.95 ) )
elif dinf == 3 :
    print (
        'O valor de R$ {:.2f} selecionando a opção de pagamento 3, o valor passa a ser duas parcelas de R$ {:.2f}'.format (
            din,
            din * 0.5 ) )
else :
    print (
        'O valor de R$ {:.2f} selecionando a opção de pagamento 4, o valor passa a ser três parcelas de R$ {:.2f}'.format (
            din,
            din / 3 ) )

# Ex.45
print ( '{:=^40}'.format ( 'Vamos jogar pedra, papel e tesoura!' ) )
print ( '''Escolha entre 
[1] Pedra
[2] Papel
[3] Tesoura''' )

from random import choice

list = [1, 2, 3]
sorteado = choice ( list )
escolha = int ( input ( 'Digite sua escolha : ' ) )
if escolha == sorteado :
    print ( 'Empatou!' )
elif escolha == 1 and sorteado == 2 or escolha == 2 and sorteado == 3 or escolha == 3 and sorteado == 1 :
    print ( 'Você perdeu!' )
else :
    print ( 'Você venceu!' )
print ( 'Sua escolha foi {} e a máquina escolheu {} !'.format ( escolha, sorteado ) )
