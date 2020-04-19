# Ex.001
print ( 'Olá Mundo!' )
# Ex.002
nome = input ( 'Qual seu nome?' )
print ( 'Prazer em te conhecer {} !'.format ( nome ) )
# Ex.003
n1 = int ( input ( 'Digite um valor numérico:' ) )
n2 = int ( input ( 'Digite um valor numérico:' ) )
s = n1 + n2
print ( 'A soma de {} com {} é igual a {}'.format ( n1, n2, s ) )
# Ex.004
a = input ( 'Digite:' )
print ( 'O tipo de {} é'.format ( a ), type ( a ) )
print ( 'É um espaço vazio?', a.isspace () )
print ( 'É numérico?', a.isnumeric () )
print ( 'É alfabético?', a.isalpha () )
print ( 'É alfanumérico?', a.isalnum () )
print ( 'Está maiúscula?', a.isupper () )
print ( 'É minúscula?', a.islower () )
print ( 'Está capitalizada?', a.istitle () )
#Ex.005
