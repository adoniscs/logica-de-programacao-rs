import os
os.system('clear')

perguntas = [ ['Seu animal gosta de bananas', 'macaco'] ]

while True:
  print('Pense em um animal...')

  acertou = False
  for pergunta in perguntas:
    respota = input(f'{pergunta[0]} (s/n): ')
    if respota.lower() == 's':
      print(f'Você pensou em {pergunta[1]}!')
      acertou = True
      break

  if not acertou:
    animal = input('Desisto! Em qual animal você pensou? ')
    novapergunta = input('Qual pergunta você faria para diferenciar esse animal? ')
    perguntas.append([ novapergunta, animal ])

  respota = input('Quer jogar novamente? (s/n): ')
  if respota.lower() != 's':
    print('Ok! Foi bom jogar com você.')
    break