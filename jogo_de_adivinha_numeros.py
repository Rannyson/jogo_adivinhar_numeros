from random import randint
from time import sleep
computador = randint(0,10) # Faz o coputador "pensar".
print ('+'*70)
print ('Vou pensar em um número entre 0 e 10. Tente adivinhar esse número...')
print ('+'*70)
jogador = int(input('Em que número eu pensei.\n')) # O jogador digite um número.
print('Xô pensar...')
sleep(4)
if jogador == computador:
    print('Parabéns, você não é tão burro quanto eu pensei.')
else:
    print('Aaaaaah,burro pra caralho, o número que eu pensei foi {} e não,{}. Tente novamente quando for mais inteligente.'.format(computador,jogador))
          
       

