from cgi import print_form
from random import randint
from time import sleep

#pensamento do computador
pc = randint(0, 5)
print('-=-' * 17)
print('Pensei em um número de 0 a 5... Adivinhe qual foi!')
print('-=-' * 17)

#usuário
jogo = int(input('O número pensado foi: '))
print('Processando...')
sleep(3)

#condições
if jogo == pc:
    print('Devo dizer que estou espantado! Você acabou de vencer uma máquina programada, parabéns!')
else:
    print('Parece que não foi dessa vez, tente a sorte novamente outro dia! O número pensado era {} e não {}!'.format(pc, jogo))