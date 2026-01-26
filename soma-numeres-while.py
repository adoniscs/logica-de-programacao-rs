import os 
os.system('clear')

qtd_repeticao = int(input('Digite quantas vezes quer que o sistema repita a soma: '))
soma = 0 
n = 1

while n <= qtd_repeticao:
  soma +=  n
  n +=  1

print(f'A soma dos números é {soma}')