# Ex.031
km = float ( input (
    'Olá, posso te ajudar? Percebi que você pretende viajar, para te ajudar vou calcular quanto sua viagem custará. Digite aqui a quilometragem que você percorrerá: ' ) )
if km < 200 :
    print ( 'Sua viagem de {} km custará R$ {:.2f}'.format ( km, (km * 1.25) ) )
else :
    print ( 'Sua viagem de {} km custará R$ {:.2f}'.format ( km, (km * 1.5) ) )
# Ex.032
from datetime import date
ano = int ( input ( 'Você deseja saber algo interessante? Digite um ano:' ) )
if ano == 0 :
    ano = date.today ().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print ( 'O ano {} é um ano bissexto'.format ( ano ) )
else :
    print ( 'O ano {} não é bissexto'.format ( ano ) )
# Ex.033
print ( 'Digite três valores e eu irei te dizer o maior e o menor' )
a = float ( input ( 'Digite o primeiro: ' ) )
b = float ( input ( 'Digite o segundo: ' ) )
c = float ( input ( 'Digite o terceiro: ' ) )
menor = a
if b < a and b < c :
    menor = b
if c < a and c < b :
    menor = c
maior = a
if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
print ( 'O menor é {:.2f}'.format ( menor ) )
print ( 'O maior é {:.2f}'.format ( maior ) )
# Ex.034
sal = float ( input ( 'Coloque aqui o salário em reais do funcionário que deseja alterar: R$ ' ) )
if sal <= 1500 :
    print (
        'O salário {} teve um aumento de 15%, com o aumento o salário atual é  R$ {:.2f}'.format ( sal, sal * 1.15 ) )
else :
    print (
        'O salário {} teve um aumento de 10%, com o aumento o salário atual é  R$ {:.2f}'.format ( sal, sal * 1.1 ) )
# Ex.035
print ( 'Vamos analisar trinagulos, digite três lados' )
l1 = float ( input ( 'Digite um lado: ' ) )
l2 = float ( input ( 'Digite um lado: ' ) )
l3 = float ( input ( 'Digite um lado: ' ) )
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 :
    print ( 'Os lados adicionados podem formar triângulos!' )
else :
    print ( 'Os lados adicionados não podem formar triângulos! Tente Outra vez !' )
