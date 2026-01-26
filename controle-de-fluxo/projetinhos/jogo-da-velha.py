# exemplo resumido da criação de um tabuleiro:
# tabuleiro = [ ['' for _ in range(3)] for _ in range(3)]

import os
os.system('clear')

tabuleiro = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' '],
]
jogador = 'X'

def exibeTabuleiro():
  for linha in tabuleiro:
    print('|'.join(linha))
    print('-' * 5)

def jogada(linha, coluna):
  tabuleiro[linha][coluna] = jogador
  if jogador == 'X':
    return 'O'
  else:
    return 'X'
  
jogador = jogada(1,1)
jogador = jogada(1,2)
exibeTabuleiro()
