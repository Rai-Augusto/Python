# Ex.036
casa = float ( input ( 'Qual o preço da casa que você deseja comprar? R$ ' ) )
salario = float ( input ( 'Qual seu salário ? R$ ' ) )
anos = int ( input ( 'Em quantos anos você pretende pagar ?' ) )
prestaçao = casa / (anos * 12)
min = salario * 0.3
if prestaçao >= min :
    print ( 'Desculpa, mas o crédito não poderá ser liberado.' )
else :
    print (
        'O crédito será liberado, as prestações a serem pagas serão de {:.2f} e deverão ser pagas dentro dos {} anos, caso contrario a devidas medidas serão tomadas.'.format (
            prestaçao, anos ) )
# Ex.037
numero = int ( input ( 'Digite um número inteiro:' ) )
print ( '''Escolha entre :
[1] - Binario
[2] - Octadecimal
[3] - Hexadecimal''' )
opçao = int ( input ( ' Qual das conversões voce escolheu ? ' ) )
if opçao == 1 :
    print ( 'O valor convertido para binário é {} do número {}'.format ( bin ( numero )[2 :], numero ) )
elif opçao == 2 :
    print ( 'O valor convertido para octadecimal é {} do número {}'.format ( oct ( numero )[2 :], numero ) )
elif opçao == 3 :
    print ( 'O valor convertido para octadecimal é {} do número {}'.format ( hex ( numero )[2 :], numero ) )
else :
    print ( 'Não é possível converter o valor.' )
# Ex.038
numero1 = int ( input ( 'Digite um número inteiro:' ) )
numero2 = int ( input ( 'Digite um número inteiro:' ) )
if numero1 > numero2 :
    print ( 'O valor {} é maior que o valor {}'.format ( numero1, numero2 ) )
elif numero1 == numero2 :
    print ( 'Os valores são equivalentes!' )
else :
    print ( 'O valor {} é menor que o valor {}'.format ( numero1, numero2 ) )
# Ex.039
from datetime import date

ano = int ( input ( 'Coloque aqui o ano de seu nascimento:' ) )
ano1 = date.today ().year
if ano1 - ano > 18 :
    print ( 'Você já se alistou ? Caso ainda não tenha vá a junta mais próxima !' )
elif ano1 - ano < 18 :
    print ( 'Você ainda não tem idade para se alistar !' )
else :
    print ( 'Você está na idade de se alistar. Fique em dia com seu país !' )
# Ex.040
nota1 = float ( input ( 'Nota 1 : ' ) )
nota2 = float ( input ( 'Nota 2 : ' ) )
media = (nota1 + nota2) / 2
if media >= 6 :
    print ( 'O aluno foi aprovado !' )
else :
    print ( 'O aluno ficou de recuperação ! Estude para não ser reprovado !' )
