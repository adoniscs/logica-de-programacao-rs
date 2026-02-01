import os
os.system('clear')

print('Olá, programador! Eu sou seu Oráculo e vou responder o que quiser!')

pergunta = input('Você quer saber sobre (Quem criou o PHP, Quem criou o Python ou qual foi o primeiro software desenvolvido)? ')

match pergunta:
  case 'Quem criou o PHP':
    print('O PHP foi criado pelo programador canadense-dinamarquês Rasmus Lerdorf em 1994')
  case 'Quem criou o Python':
    print('O Python foi criado pelo programador holandês Guido van Rossum em 1989, no instituto CWI, na Holanda.')
  case 'qual foi o primeiro software desenvolvido':
    print('O primeiro software (ou algoritmo) da história foi desenvolvido por Ada Lovelace na década de 1840')
  case _:
    print('Desculpe, mas sabe o que é? Ainda estou aprendendo sobre esse mundo da programação...')