# Ex.061
n1 = int ( input ( 'Digite o primeiro termo: ' ) )
r = int ( input ( 'Digite a razão: ' ) )
t = n1
c = 1

while c <= 10 :
    print ( '{} '.format ( t ) )
    t += r
    c += 1

# Ex.62
primeiro = int ( input ( 'Primeiro termo: ' ) )
razao = int ( input ( 'Digite a razão: ' ) )
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0 :
    total = total + mais
    while contador <= total :
        print ( '{}'.format ( termo ) )
        termo += razao
        contador += 1
    mais = int ( input ( 'Quer ver mais quantos termos? ' ) )
print ( 'Obrigado!' )

# Ex.063

numtermos = int ( input ( 'Quantos termos : ' ) )

n1, n2 = 0, 1
cont = 0

if numtermos <= 0 :
    print ( 'Por Favor, adicione termos positivos!' )
elif numtermos == 1 :
    print ( 'Fibonacci', numtermos, ":" )
    print ( n1 )
else :
    print ( "Fibonacci:" )
    while cont < numtermos :
        print ( n1 )
        nth = n1 + n2
        n1 = n2
        n2 = nth
        cont += 1

# Ex.064

num = contagem = soma = 0

while num != 999 :
    num = int ( input ( 'Digite 999 para parar : ' ) )
    contagem += 1
    soma += num
print ( 'Você digitou {} valores e a soma desses valores é {}'.format ( contagem, soma - 999 ) )

# Ex.065

con = soma = number = maior = menor = 0
resp = 'S'

while resp in 'Ss' :
    soma += number
    con += 1
    if number == 0 :
        maior = menor = number
    else :
        if number > maior :
            maior = number
        if number < menor :
            menor = number
    number = int ( input ( 'Digite um valor : ' ) )
    resp = str ( input ( 'Deseja continuar ? [S/N] ' ) ).upper ().strip ()[0]
media = soma / (con)
print ( '{} - Média / {} - Número de termos '.format ( media, con, ) )
