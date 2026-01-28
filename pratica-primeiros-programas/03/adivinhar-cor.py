import os
os.system('clear')

print('Vamos juntos criar uma história descontraída e muito maluca.')
print('Para isso, preciso que escreva 6 palavras, na seguinte ordem: ')
print('Lugar; pessoa famosa; objeto; cor; verbo; número')
palavras = []

for palavra in range(6):
  palavra = input('Digite uma palavra: ')
  palavras.append(palavra)

os.system('clear')

print('Com base nas palavras fornecidas, vou montar uma história maluca... ')
input('Aperte enter para ver o resultado')

print(f'Um dia, no(a) {palavras[0]}, encontrei com o(a) {palavras[1]} segurando um(a) {palavras[2]} {palavras[3]}. Ele(a) começou a {palavras[4]} sem parar, e isso durou por {palavras[5]} horas!')
