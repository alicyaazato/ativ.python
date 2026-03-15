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

#6. Data por extenso: Leia uma data (dd/mm/aaaa) e mostre no formato
#  '29 de Outubro de 1973'.
"""
data = input("Digite a data (dd/mm/aaaa): ")
dia, mes, ano = data.split('/')

m = int(mes)

if m == 1:
    extenso = "Janeiro"

elif m == 2:
    extenso = "Fevereiro"

elif m == 3:
    extenso = "Março"

elif m == 4:
    extenso = "Abril"

elif m == 5:
    extenso = "Maio"

elif m == 6:
    extenso = "Junho"

elif m == 7:
    extenso = "Julho"

elif m == 8:
    extenso = "Agosto"

elif m == 9:
    extenso = "Setembro"

elif m == 10:
    extenso = "Outubro"

elif m == 11:
    extenso = "Novembro"

elif m == 12:
    extenso = "Dezembro"

else:
    extenso = "Mês Inválido, tente novamente"

print(f"{dia} de {extenso} de {ano}")
"""


#7. Contar espaços e vogais: Dada uma frase, conte quantos espaços existem e
#  quantas vezes aparecem as vogais.
"""
frase = input("Digite uma frase: ").lower()
espacos = 0
vogais = 0
lista_vogais = "aeiou"

for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in lista_vogais:
        vogais += 1

print(f"Espaços: {espacos}")
print(f"Vogais: {vogais}")
"""


#8. Palíndromo: Leia uma sequência de caracteres e informe se é um palíndromo.

"""
def eh_palindromo(texto):
    texto_limpo = texto.replace(" ", "").lower()
    return texto_limpo == texto_limpo[::-1]

entrada = input("Digite a palavra ou frase: ")
if eh_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
"""



#9. Verificação de CPF: Leia um CPF no formato xxx.xxx.xxx-xx e valide os
#  dígitos verificadores.


"""
cpf_entrada = input("Digite o CPF (xxx.xxx.xxx-xx): ")

cpf = cpf_entrada.replace('.', '').replace('-', '')

soma = 0
peso = 10
for i in range(9):
    soma = soma + int(cpf[i]) * peso
    peso = peso - 1

d1 = (soma * 10) % 11
if d1 > 9: d1 = 0

soma = 0
peso = 11
for i in range(10):
    soma = soma + int(cpf[i]) * peso
    peso = peso - 1

d2 = (soma * 10) % 11
if d2 > 9: d2 = 0


if str(d1) == cpf[9] and str(d2) == cpf[10]:
    print("CPF Válido!")
else:
    print("CPF Inválido!")



"""


#10. Número por extenso: Leia um número até 99 e mostre-o por extenso.


"""
n = input("Digite um número de 0 a 99: ")

unidades = ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", 
            "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]

dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]

# Se o número for menor que 20, pegamos direto na primeira lista
if int(n) < 20:
    print(unidades[int(n)])
else:
    d = int(n[0]) # Primeiro número (dezena)
    u = int(n[1]) # Segundo número (unidade)
    
    if u == 0:
        print(dezenas[d])
    else:
        print(dezenas[d] + " e " + unidades[u])


"""




#11. Jogo da Forca: Desenvolva um jogo simples da forca usando uma lista 
# de palavras.

"""
import random

palavras = ['banana', 'python', 'casa', 'monitor']
palavra = random.choice(palavras)
palpite = "" 
tentativas = 6

while tentativas > 0:
    ganhou = True
    for letra in palavra:
        if letra in palpite:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            ganhou = True 

    if ganhou:
        print("\nVocê ganhou!")
        break

    chute = input("\nDigite uma letra: ")
    palpite += chute

    if chute not in palavra:
        tentativas -= 1
        print(f"Erro! Vidas: {tentativas}")
else:
    print(f"Perdeu! A palavra era: {palavra}")


"""




#12. Corrigir telefone: Leia um telefone com 7 ou 8 dígitos e ajuste
#  adicionando o '3' se necessário.

"""

def corrigir_telefone(telefone):
    telefone = telefone.replace("-", "").replace(" ", "")
    
    tamanho = len(telefone)
    
    if tamanho == 7:
        telefone_corrigido = "3" + telefone
        print(f"Telefone corrigido: {telefone_corrigido}")
    elif tamanho == 8:
        print(f"Telefone já possui 8 dígitos: {telefone}")
    else:
        print("Quantidade de dígitos inválida para este ajuste.")

num = input("Digite o telefone (7 ou 8 dígitos): ")
corrigir_telefone(num)
"""




#13. Palavra embaralhada: Mostre uma palavra com letras embaralhadas e 
# permita que o usuário adivinhe.

"""
import random

# A palavra que o usuário deve adivinhar
palavra_x = "PYTHON"

# Embaralha as letras da palavra
embaralhada = "".join(random.sample(palavra_x, len(palavra_x)))

print(f"Adivinhe a palavra: {embaralhada}")

# Pede o palpite do usuário
chute = input("Qual é a palavra original? ").upper()

# Verifica se ele acertou
if chute == palavra_x:
    print("Parabéns, você acertou!")
else:
    print(f"ERRADA! A palavra era: {palavra_x}")
"""


#14. Leet Speak: Leia um texto e converta para a escrita estilo leet (ex: 1337).
"""""
texto = input("Digite o texto: ").upper()
leet = ""

for letra in texto:
    if letra == 'A':
        leet += '4'
    elif letra == 'E':
        leet += '3'
    elif letra == 'I':
        leet += '1'
    elif letra == 'O':
        leet += '0'
    elif letra == 'T':
        leet += '7'
    elif letra == 'S':
        leet += '5'
    else:
        leet += letra  
print(leet)
"""

