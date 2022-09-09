###################################################################################
# Projeto:  Gerando palpites para Megasena 
# Objetivo: Gerar palpites aleatórios para sorteios da Megasena
###################################################################################

from random import randint
from time import sleep

lista = list()
jogos = list()
print (('=' * 50) + '\n            PALPITES PARA MEGA SENA\n' + ('=' * 50))
quant = int(input('Quantos palpites você deseja ? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('\n' + ('*' * 10) + f'  GERANDO {quant} PALPITES  ' + ('*' * 10))
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print ('\n' + ('-' * 20) + ' BOA SORTE ' + ('-' * 20))

