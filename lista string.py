#1. Tamanho de strings: Leia duas strings, mostre o conteúdo e o tamanho de cada uma. 
# Informe se possuem o mesmo tamanho e se o conteúdo é igual ou diferente.

"""
str1 = input("Digite a primeira frase: ")
str2 = input("Digite a segunda frase: ")

print(f"\nString 1: '{str1}' (Tamanho: {len(str1)})")
print(f"String 2: '{str2}' (Tamanho: {len(str2)})")


if len(str1) == len(str2):
    print("As duas tem o mesmo tamanho.")
else:
    print("As duas tem tamanhos diferentes.")

if str1 == str2:
    print("É igual.")
else:
    print("É diferente.")

"""

# 2. Nome ao contrário em maiúsculas: Leia o nome do usuário
# e mostre-o de trás para frente em letras maiúsculas.

"""
nome = input("Digite o seu nome em letra MAIUSCULA: ")

contrario = nome[::-1]

print("De trás pra frente" , contrario)"""

#3. Nome na vertical: Solicite o nome do usuário e imprima cada 
# letra em uma linha.
"""
nome = input("Digite o seu nome: ")

for letra in nome:
    print(letra)"""


#Nome em escada: Mostre o nome em formato de escada
#crescente (F, FU, FUL...).

"""nome = input("Digite o seu nome: ")
i = 1
for i in range(len(nome)):
    print(nome[:i+1])"""

#5. Escada invertida: Mostre o nome em escada decrescente.

"""nome = input("Digite o seu nome: ")
i=1
for i in range(len(nome), 0, -1 ):
    print(nome[:i])"""

print("teste")