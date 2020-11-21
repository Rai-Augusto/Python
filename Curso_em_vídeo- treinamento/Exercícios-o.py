#Ex.071
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro','Cinco')
while True:
    x = int(input('Digite um valor entre 0 e 5: '))
    if 0 <= x <= 5:
        break
    print('Tente outra vez. ', end = '')
print(f'{cont[x]}')

#Ex.072
from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados são: ',end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\n{max(numeros)} é o maior!')
print(f'{min(numeros)} é o menor!')

#Ex.073
y =(int(input('Digite um valor: ')), 
    int(input('Digite um valor: ')), 
    int(input('Digite um valor: ')), 
    int(input('Digite um valor: ')))

print(f'Você digitou {y}')
print(f'O maior é {max(y)}!')
print(f'O menor é {min(y)}!')
print('Os valores pares são : ', end='')
for i in y:
    if i % 2 == 0:
        print(f'{i}',end=' ')

#Ex.074
lista = ('Lápis', 2.00,'Borracha', 1.00,'Caneta', 2.00,'Mochila', 50.00,'Estojo', 11.00,'Lapiseira', 9.90)
print('-'*40)
print('Lista de preços:')
print('-'*40)

for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)

#Ex.075
palavras = ('Cantar','ter','encantar', 'interar')
for p in palavras:
    for letra in p :
        if letra.lower() in 'aeiou':
            print(letra,end='')