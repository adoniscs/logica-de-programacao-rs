import os
os.system("clear")

print("sistema para saber se o aluno esta: 'aprovado', 'reprovado' ou 'de recuperação'\n")
nota = float(input("Digite sua nota: "))

if nota >= 7:
  print("Aprovado")
elif nota < 5:
  print("Reprovado")
else:
  print("Recuperação")