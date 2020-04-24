#Ex.021 - ainda não finalizado
import pygame
pygame.init()
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()
#Ex.022
nome = str(input('Coloque aqui seu nome completo:')).strip()
print('Analisando seu nome observei que ...')
print('Seu nome passando para maiúsculo fica {} ' .format(nome.upper()))
print('Seu nome passando para minúsculo fica {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print ('Seu primeiro nome {} tem {} letras' .format(separa [0], len(separa [0])))
#Ex.023
num= int(input('Digite aqui um número:'))
print ('O número {} tem unidade {} ' .format(num, num//1 % 10 ))
print ('O número {} tem dezena {} ' .format(num, num//10 % 10))
print ('O número {} tem centena {}' .format(num,num//100 % 10))
print ('O número {} tem milhar {}' .format(num, num// 1000 % 100))
#Ex.024
cit = str(input('Em qual cidade você nasceu?')).strip()
print (cit[:2].upper()=='SP')
#Ex.025
nome2= str(input('Qual seu nome?'))
print ('Seu nome tem Augusto? {}' .format('Augusto' in nome2))
