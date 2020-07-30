# Ex.066

while True :
    tabuada = int ( input ( 'Qual tabuada deseja ?' ) )
    if tabuada == 0 :
        break
    for tab in range ( 0, 11 ) :
        print ( '{} X {:2} = {}'.format ( tabuada, tab, tabuada * tab ) )
print ( 'Fim!' )

# Ex.067
from random import randint

v = 0
while True :
    player = int ( input ( 'Digite um número:' ) )
    computer = randint ( 0, 10 )
    tot = (player + computer)
    tipo = ' '
    while tipo not in 'PI' :
        tipo = str ( input ( 'Par ou Ímpar ? [P/I]' ) ).strip ().upper ()
    print ( f'O jogador jogou {player} e a máquina {computer} com total {tot}' )
    print ( 'Deu par !' if tot % 2 == 0 else 'Deu ímpar !' )
    if tipo == 'P' :
        if tot % 2 == 0 :
            print ( 'Win!' )
            v += 1
        else :
            print ( 'Lose!' )
            break
    elif tipo == 'I' :
        if tot % 2 == 1 :
            print ( 'Win!' )
            v += 1
        else :
            print ( 'Lose!' )
            break
        print ( 'Outra vez ?' )
print ( f'Chega! Você venceu {v} vezes !' )

# Ex.068
h = 0
m = 0
maior18 = 0

while True :
    nome = str ( input ( 'Nome:' ) )
    idade = int ( input ( 'Idade: ' ) )
    sexo = ' '
    while sexo not in 'HM' :
        sexo = str ( input ( 'Sexo: [H/M]' ) ).strip ().upper ()[0]
    if idade >= 18 :
        maior18 += 1
    if sexo == 'H' :
        h += 1
    else :
        m += 1
    resposta = ' '
    while resposta not in 'SN' :
        resposta = str ( input ( 'Quer continuar ? [S/N]' ) ).strip ().upper ()[0]
    if resposta == 'N' :
        break
print ( f'Fim! Temos {h} homens e {m} mulheres, com maioridade temos {maior18}' )

# Ex.069
total = caro = barato = cont = 0
menor = ' '
maior = ' '

while True :
    produto = str ( input ( 'Digite o nome do produto : ' ) )
    preco = float ( input ( 'Qual o preço : ' ) )
    cont += 1
    total += preco

    if cont == 1 :
        caro = preco
        barato = preco
    else :
        if preco < barato :
            barato = preco
        if preco > caro :
            caro = preco

    resp = ' '
    while resp not in 'SN' :
        resp = str ( input ( 'Quer continuar ?[S/N]' ) ).strip ().upper ()[0]
    if resp == 'N' :
        break
print ( f'O total é {total:.2f} o produto mais caro é R$ {caro:.2f} e o mais barato é R$ {barato:.2f}' )

# Ex.070
print ( 'Banco 24horas' )
dinheiro = int ( input ( 'Qual valor você quer sacar ? R$' ) )
tudo = dinheiro
c = 100
totc = 0
while True :
    if tudo >= c :
        tudo -= c
        totc += 1
    else :
        if totc > 0 :
            print ( f'Total de cédulas {totc} de R$ {c}' )
        if c == 100 :
            c = 50
        elif c == 50 :
            c = 20
        elif c == 20 :
            c = 10
        elif c == 10 :
            c = 5
        elif c == 5 :
            c = 2
        elif c == 2 :
            c = 1
        totc = 0
        if tudo == 0 :
            break
