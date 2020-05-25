# Ex.046
for cont in range ( 10, -1, -1 ) :
    print ( cont )
print ( 'Acabou !' )

# Ex.047
for cont in range ( 1, 51 ) :
    if cont % 2 == 0 :
        print ( cont, end=' ' )

# Ex.048
s = 0
c = 0
for i in range ( 1, 11 ) :
    if i % 2 != 0 :
        c = c + 1
        s = s + i
        print ( i, end=' ' )
print ( 'A soma de todos valores solicitados é {}'.format ( s ) )

# Ex.049
tab = int ( input ( 'Digite um numero: ' ) )
for tabuada in range ( 0, 11 ) :
    print ( '{} X {:2} = {}'.format ( tab, tabuada, tab * tabuada ) )

# Ex.050
soma = 0
contagem = 0
for a in range ( 1, 7 ) :
    num = int ( input ( 'Digite o valor {}: '.format ( a ) ) )
    if num % 2 == 0 and num != 0 :
        soma += num
        contagem += 1
print ( 'Os números pares contados foram {} e a soma deles foi de {}'.format ( contagem, soma ) )
