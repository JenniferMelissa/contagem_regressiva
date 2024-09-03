# adiciona ao seu programa comandos que nao estao disponiveis de forma global, na nossa maquina, e o import torna os comandos disponiveis

#importacao de bilbioteca
import os
import time

#entrada de dados
numero = int(input('Informe um número inteiro: '))


print('\n Contagem Regressiva: ')

while numero >= 0:
    os.system('cls') #comando de limpar, do prompt de comando
    print(f'{numero} ...')
    numero -= 1
    time.sleep(1)

os.system('cls') #esta fora do while devida a identacao
print('KABUMMMMMMMMMMMMMMMMMMMMMMM!!!!!!!!!!!!')
 #funcao sleep dentro da biblioteca time, trava o programa por uma quantidade de tempo, e é medido em segundo, não entende milesimo de segundos
 #os é uma biblioteca magica, ela traz comandos do computador nativo, comandos do prompt de comando
 #apos a contagem vai aparecer a mensagem Kabum