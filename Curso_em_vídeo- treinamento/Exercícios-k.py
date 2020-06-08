# Ex.051
print ( 'Vamos Estudar Progressões!' )
a1 = int ( input ( 'Digite o primeiro termo de sua Progressão: ' ) )
n = int ( input ( 'Digite o número de termos de sua Progressão: ' ) )
r = int ( input ( 'Digite a razão que irá reger sua Progressão: ' ) )
q = r
an = a1 + (n - 1) * r
an1 = a1 * (q ** (n - 1))
print ( 'O valor do último termo da sua Progressão Aritmetica é o {} e de sua geométrica é {}'.format ( an, an1 ) )

# Ex.052
num = int ( input ( 'Digite um valor: ' ) )
contagem = 0
for c in range ( 1, num + 1 ) :
    if num % c == 0 :
        print ( '\033[34m', end=' ' )
        contagem += 1
    else :
        print ( '\033[m', end=' ' )
    print ( '{}'.format ( c ), end=' ' )

print ( 'O número {} possui {} divisores !'.format ( num, contagem ), end=' ' )
if contagem == 2 :
    print ( 'É primo!' )
else :
    print ( 'Não é primo!' )

# Ex.053
from datetime import date

atual = date.today ().year
for pessoas in range ( 0, 3 ) :
    nasc = int ( input ( 'Digite o ano que você nasceu : ' ) )
    idade = atual - nasc
    if idade >= 18 :
        print ( 'Maior de idade !' )
    else :
        print ( 'Menor de idade !' )

# Ex.054
maior = 0
menor = 0
for m in range ( 1, 4 ) :
    p = float ( input ( 'Digite sua massa corporal {}: '.format ( m ) ) )
    if p == 1 :
        maior = p
        menor = p
    else :
        if p > maior :
            maior = p
        else :
            menor = p
print ( 'O maior é {} e o menor {} '.format ( maior, menor ) )

# Ex.055
maioridade = 0
menoridade = 0
somaidade = 0
mediaidade = 0
totalhomens = 0
totalmulheres = 0

for pessoas in range ( 1, 4 ) :
    print ( 'A pessoa Nº {}'.format ( pessoas ) )
    nome = str ( input ( 'Nome: ' ) ).strip ().upper ()
    idade0 = int ( input ( 'Idade: ' ) )
    sexo = str ( input ( 'Sexo [H/M]: ' ) ).strip ().upper ()
    somaidade += idade0
    mediaidade = somaidade / 3
    if sexo in 'Hh' :
        totalhomens += 1
    if sexo in 'Mm' :
        totalmulheres += 1
    else :
        print ( 'Apenas H/M' )
    if maioridade == 1 :
        maioridade = idade0
        menoridade = idade0
    else :
        if idade0 > maioridade :
            maioridade = idade0

print ( 'A média das idades é {:.2f} a maior idade é {} '.format ( mediaidade, maioridade ) )
print ( 'O número de homens é {} e de mulheres é {} '.format ( totalhomens, totalmulheres ) )
