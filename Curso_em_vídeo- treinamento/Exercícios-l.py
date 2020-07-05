# Ex.056

M = 0
F = 0
somaidade = 0
maioridade = 0
menoridade = 0
nomevelho = ''
nomenovo = ''
for i in range ( 1, 5 ) :
    print ( '-------------------' )
    nome = str ( input ( 'Nome: ' ) ).strip ().upper ()
    idade = int ( input ( 'Idade: ' ) )
    sexo = str ( input ( 'Sexo [M/F]: ' ) ).upper ().strip ()
    somaidade += idade
    média = somaidade / 4
    if sexo in 'Mm' :
        M += 1
    else :
        F += 1
    if maioridade == 1 :
        maioridade = idade
        menoridade = idade

    else :
        if idade > maioridade :
            maioridade = idade
            nomevelho = nome
        else :
            menoridade = idade
            nomenovo = nome
print ( 'A soma das idades é igual a {} e a média é {}'.format ( somaidade, média ) )
print ( 'A maior idade é de {} que tem {} anos e a menor idade é de {} e tem {} anos'.format ( nomevelho, maioridade,
                                                                                               nomenovo, menoridade ) )

if M > F :
    print ( 'O número de homens é {} e o de mulheres é {}'.format ( M, F ) )
elif M == F :
    print ( 'O número de indivíduos homens e mulheres é igual' )
else :
    print ( 'O número de mulheres é {} e o de homens é {}'.format ( F, M ) )

# Ex.057
a = str ( input ( 'Qual seu sexo [M/F] ?' ) ).strip ().upper ()[0]
while a not in 'MmFf' :
    a = str ( input ( 'Tente outra vez: ' ) ).strip ().upper ()
print ( 'Seu sexo {} foi registrado com sucesso!'.format ( a ) )

# Ex.058
from random import randint

comp = randint ( 0, 10 )
cont = 1
tent = int ( input ( 'Tentativa :' ) )
acerto = False
while not acerto :
    tent = int ( input ( 'Tente outra vez! Qual a sua nova tentativa ? ' ) )
    cont += 1
    if tent == comp :
        acerto = True
print ( 'Acertou! Com {} tentativas'.format ( cont ) )

# Ex.059
v1 = int ( input ( 'Digite um valor inteiro:' ) )
v2 = int ( input ( 'Digite outro valor inteiro:' ) )
opção = 0
while opção != 5 :
    print ( ''' [1] Soma
    [2] Multiplicação 
    [3] Maior valor 
    [4] Novos Valores 
    [5] Sair do Programa''' )
    opção = int ( input ( 'Qual sua escolha ? ' ) )
    if opção == 1 :
        soma = v1 + v2
        print ( 'O valor da soma entre {} e {} é {} '.format ( v1, v2, soma ) )
    elif opção == 2 :
        mult = v1 * v2
        print ( 'O valor da multiplicação entre {} e {} é {} '.format ( v1, v2, mult ) )
    elif opção == 3 :
        if v1 > v2 :
            maior = v1
        else :
            maior = v2
        print ( 'O maior valor entre {} e {} é {}'.format ( v1, v2, maior ) )
    elif opção == 4 :
        print ( 'Informe os valores novamente' )
        v1 = int ( input ( 'Digite um valor inteiro:' ) )
        v2 = int ( input ( 'Digite outro valor inteiro:' ) )
    else :
        print ( 'Tente outra vez!' )
print ( 'Fim do Programa. Volte sempre!' )

# Ex.060
from math import factorial

num = int ( input ( 'Digite um número:' ) )
fat = factorial ( num )
print ( 'O fatorial de {} é {}'.format ( num, fat ) )
