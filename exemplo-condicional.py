import os
os.system('clear')

print("Bem vindo ao DETRAN!")
print("Este é o novo teste extremamente complexo para liberar ou não a CNH\n")

idade = int(input("Digite a sua idade: "))

if idade >= 18:
  print("Pode dirigir!")
else:
  print("Não pode dirigir!")
print("Acabou!")