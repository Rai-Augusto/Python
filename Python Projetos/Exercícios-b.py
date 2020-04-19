# Ex.006
n = int ( input ( ' Digite um número:' ) )
print ( 'O dobro de {} é {}'.format ( n, n * 2 ) )
print ( 'O triplo de {} é {}'.format ( n, n * 3 ) )
print ( 'A raiz quadrada de {} é igual a {}'.format ( n, (n ** (1 / 2)) ) )
# Ex.007
n1 = float ( input ( 'Nota p1:' ) )
n2 = float ( input ( 'Nota p2:' ) )
nf = (n1 + n2) / 2
print ( 'A nota final foi: {:.1f}'.format ( nf ) )
if nf > 6 :
    print ( 'O aluno foi aprovado.' );
else :
    print ( 'O aluno está de recuperação.' )
# Ex.008
m = float ( input ( 'Coloque aqui a medida em metros que você deseja converter:' ) )
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m * (1 / 10)
hm = m * (1 / 100)
km = m * (1 / 1000)
print ( 'O valor em mm é {}'.format ( mm ) )
print ( 'O valor em cm é {}'.format ( cm ) )
print ( 'O valor em dm é {}'.format ( dm ) )
print ( 'O valor em dam é {}'.format ( dam ) )
print ( 'O valor em hm é {}'.format ( hm ) )
print ( 'O valor em km é {}'.format ( km ) )
#Ex.009
tab= int(input('Deseja saber a tabuadada de qual número?'))
print( ' {} x {:2} = {}' . format(tab, 1, tab*1))
print( ' {} x {:2} = {}' . format(tab, 2, tab*2))
print( ' {} x {:2} = {}' . format(tab, 3, tab*3))
print( ' {} x {:2} = {}' . format(tab, 4, tab*4))
print( ' {} x {:2} = {}' . format(tab, 5, tab*5)) 
print( ' {} x {:2} = {}' . format(tab, 6, tab*6))
print( ' {} x {:2} = {}' . format(tab, 7, tab*7))
print( ' {} x {:2} = {}' . format(tab, 8, tab*8))
print( ' {} x {:2} = {}' . format(tab, 9, tab*9))
print( ' {} x {:2} = {}' . format(tab, 10, tab*10))
#Ex.010
din = float ( input ('Olá, você deseja fazer conversâo de qual valor para Dólar e Euro?'))
dol = din / 5.240
eur = din / 5.70
print( 'Você conseguirá comprar com {} aproximadamente {:.2f} em Dólar e em {:.2f} Euro.' .format(din,dol,eur))



