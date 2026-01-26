import os
os.system('clear')

print('Olá, eu sou a Sofia, sua assistente pessoal! O que você quer fazer hoje?')
comando = input('Digite um comando: ')

match comando:
  case 'oi' | 'olá':
    print('Oi, como vai você?')
  case 'tchau' | 'sair' | 'fim':
    print('Tchau! Foi bom conversar com você.')
  case 'piada':
    print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login')
  case 'clima' | 'previsão do tempo':
    print('Está MUUUUUUUUITO quente! Deve ter passado de 40ºC 🥵')
  case _:
    print('Desculpe, não entendi o comando')