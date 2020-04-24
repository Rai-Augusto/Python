#Ex.011
l1 = float(input('Coloque o tamanho da altura em m do cubo:'))
l2 = float(input('Coloque o tamanho da base em do cubo:'))
l3 = float(input('Coloque o tamanho da profundidade em m do cubo:'))
vol = l1 * l2 *l3
print ('O volume do cubo de altura {}, de base {} e profundidade {} é {} metros cúbicos e {} litros' .format(l1, l2, l3, vol, vol * 1000))
#Ex.012
prod= float (input('Qual o preço do produto desejado? R$ '))
print ('O produto desejado R$ {:.2f}, está em promoção e com desconto de 20% custando RS{:.2f} ' .format (prod, prod * (80/100)))
#Ex.013
sal = float(input ('Coloque aqui o salário do funcionário para ser reajustado: R$'))
rea = float(input('Coloque aqui o valor numérico da porcentagem do reajuste:'))
print ('O valor do salário {} reajustado com porcentagem {}% é igual a {}' .format( sal, rea, sal * (1+ rea/100)))
#Ex.014
t = float( input ('Qual a temperatura que deseja converter em °C:'))
print ('A temperatura {:.1f} em Fahrenheit vale {:.1f}°F e em Kelvin {:.2f}°K' .format( t, (t*9/5) + 32 , t + 273,16))
#Ex.015
dias = int(input('Por quantos dias você alugou nosso veículo ?'))
km = float( input ('Quantos quilometros você rodou?'))
print('O valor a ser pagos por {} dias e {} quilometros rodados é {}' .format(dias, km, (dias *100) + (km*25)))