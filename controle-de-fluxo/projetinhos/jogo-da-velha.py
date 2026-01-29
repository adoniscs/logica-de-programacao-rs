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

exibeTabuleiro()

def jogada(linha, coluna):
  if (
    not 0 <= linha <= 2 or 
    not 0 <= coluna <= 2 or 
    tabuleiro[linha][coluna] != ' '
  ):
    print('Jogada inválida!')
    return jogador
  
  tabuleiro[linha][coluna] = jogador
  
  return 'O' if jogador == 'X' else 'X'

def temGanhador():
  """ veridfica as linhas """
  for linha in range(3):
    if(
      tabuleiro[linha][0] != ' ' and
      tabuleiro[linha][0] == tabuleiro[linha][1] and
      tabuleiro[linha][0] == tabuleiro[linha][2]
    ):
      print(f'{tabuleiro[linha][0]} GANHOU')
      return True
    
  """ verifica as colunas """
  for coluna in range(3):
    if(
      tabuleiro[0][coluna] != ' ' and
      tabuleiro[0][coluna] == tabuleiro[1][coluna] and
      tabuleiro[0][coluna] == tabuleiro[2][coluna]
    ):
      print(f'{tabuleiro[0][coluna]} GANHOU')
      return True
    
  """ verifica as diagonais """
  if (
      tabuleiro[1][1] != ' ' and
      (
        (
          tabuleiro[0][0] == tabuleiro[1][1] and
          tabuleiro[0][0] == tabuleiro[2][2]  
        ) or
        (
          tabuleiro[0][2] == tabuleiro[1][1] and
          tabuleiro[1][1] == tabuleiro[2][0]  
        )
        
      )
  ):
    print(f'{tabuleiro[1][1]} GANHOU')
    return True

  """ se não teve ganhador em nenhuma forma """
  return False

def temEmpate():
  for linha in range(3):
    for coluna in range(3):
      if tabuleiro[linha][coluna] == ' ':
        return False
  print('EMPATE')
  return True

while True:
  try:
    linha = int(input('Digite a linha: '))
    coluna = int(input('Digite a coluna: '))
    jogador = jogada(linha, coluna)
  except (ValueError, IndexError):
    print('Digite valores númericos entre 0 e 2')

  print(f'Jogador da vez: {jogador}')
  exibeTabuleiro()

  if temGanhador() or temEmpate():
      break
  