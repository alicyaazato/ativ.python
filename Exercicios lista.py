
# 1. Faça um programa que mostre a mensagem: 'Alô mundo'.

"""print("Alô mundo")"""


#2. Faça um programa que peça um número e então mostre a mensagem:
#  O número informado foi
#[número].

"""numero = input("Digite um numero: ")
print("O numero informado é: ", numero)"""

#3. Faça um programa que peça dois números e imprima a soma.

"""num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
x = num1 + num2
print("Os numeros são: " , x )"""

#4. Faça um programa que peça as 4 notas bimestrais e mostre a média.

"""nota1 = int(input("digite a 1° nota : "))
nota2 = int(input("digite a 2° nota : "))
nota3 = int(input("digite a 3° nota : "))
nota4 = int(input("digite a 4° nota : "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média bimestral é: " , media )"""

#5. Faça um programa que converta metros para centímetros.

"""metros = float(input("digite um numero : "))
centimetros = metros * 100

print("O valor em centimetros é: " , centimetros)"""

#Faça um programa que peça o raio de um círculo, 
#calcule e mostre sua área.

"""raio = float(input("digite o raio de um círculo : "))

area = 3.14 * (raio ** 2)

print("Valor da area é: " , area)"""

#Faça um programa que calcule a área de um quadrado e 
#mostre o dobro desta área.

"""lado = float(input("digite a área de um quadrado : "))
area = lado * 2
dobro_area = area * 2

print(f"A area do quadrado é: {area}, e o dobro é: {dobro_area}" )"""

#8. Faça um programa que pergunte quanto você ganha por hora e o número de 
# horas trabalhadas no mês. Calcule e mostre o salário total do mês.

"""horas = float(input("Quanto você ganha por hora? "))
valor_trabalhado = float(input("E as suas horas trabalhadas? "))

total = horas * valor_trabalhado

print(f"O salario no mês é : {total:.2f}")"""

#9. Faça um programa que peça a temperatura em Fahrenheit e 
# converta para Celsius. Fórmula: C = 5* ((F - 32) / 9).

"""f = float(input("Digite a temperatura em Fahrenheit: "))
c = 5* ((f - 32) / 9)

print(f"{f}°F equivale a {c:.2f}°C")"""

#10. Faça um programa que peça a temperatura em Celsius e 
# converta para Fahrenheit. Fórmula: F = (C * 9/5) + 32.

"""c = float(input("Digite a temperatura em Celsius: "))
f = (c * 9/5) + 32.
print(f"{c}°C é igual a {f:.2f}°F")"""

#11. Peça dois números inteiros e um número real. Calcule: 
# (a) o produto do dobro do primeiro com metade do segundo; 
# (b) a soma do triplo do primeiro com o terceiro; 
# (c) o terceiro elevado ao cubo.

"""num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

print("Primeiro numero inteiro :", (2 * num1) * (num2 / 2))
print("Segundo numero inteiro :", (3 * num1) + real)
print("Numero real :", real ** 3)"""

# 12. Converta um valor em Gigabytes para Megabytes. 
# Fórmula: MB = GB * 1024.

"""GB = float(input("Digite o um valor em Gigabytes : "))
MB = MB = GB * 1024.
print(f"O valor de gigabytes {GB} para Mmegabytes é: {MB:.2f}  ")"""

#13. Converta um valor em Gigabytes para Megabytes e Kilobytes
"""GB = float(input("Digite o valor em Gigabytes: "))
MB = GB * 1024
KB = MB * 1024

print(f"Gigabytes equivale a: {GB}\nEm megabytes: {MB:,.2f}\nEm kilobytes : {KB:,.2f}")"""


# """
# 14. Um pescador paga multa de R$4,00 por quilo excedente caso ultrapasse 50 kg de peixes. Faça
# um programa que calcule excesso e multa.
"""peso = float(input("Digite o peso total de peixes (kg): "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print(f"Excesso: {excesso:.2f} kg")
print(f"Multa: R$ {multa:.2f}")"""

#15. Faça um programa que calcule o salário com descontos: 
# IR (11%), INSS (8%) e Sindicato (5%). Mostrar salário bruto e líquido.
"""
salario_bruto = 2000.0
inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (sindicato+ir+inss)

print("INSS: ", inss)
print("IR: ", ir)
print("Sindicato: ", sindicato)
print("Salario liquido: ", salario_liquido)
print("Salario bruto: ", salario_bruto)"""

#16. Uma loja de tintas precisa calcular quantas latas comprar. 1 litro cobre 3 m2, 
# uma lata tem 18 litros e custa R$80.
"""
area = int(input("Insira qual o tamanho da area a ser pintada em m2: "))

litros_necessario = (area*1)/3

latas = 0 
print("A quantidade de litros necessarios na area ",area, "é ", litros_necessario)
while litros_necessario > 0:
    litros_necessario = litros_necessario - 18
    latas = latas + 1
valor = latas * 80 
print("O valor total a ser conprado é: ", valor, " pois a quantidade de latas é: ", latas)
"""

# #17. Versão avançada da tinta: 1 litro cobre 6 m2. Lata 18L (R$80) e galão 3,6L (R$25). Calcular
# melhor opção com 10% de folga.

"""
area = float(input("Insira qual o tamanho da area a ser pintada em m2: "))

litros_necessario = (area*1)/3

litros_necessario_galoes = litros_necessario
litros_necessario_latas = litros_necessario
latas = 0 
print("A quantidade de litros necessarios na area ",area, "é ", litros_necessario)
while litros_necessario_latas > 0:
    litros_necessario_latas = litros_necessario_latas - 18
    latas = latas + 1
    
galoes = 0 
while litros_necessario_galoes > 0:
    litros_necessario_galoes = litros_necessario_galoes - 3.6
    galoes = galoes +1
valor_galoes = galoes * 25
valor_latas = latas * 80

desc_gal = valor_galoes * 0.10
desc_lat = valor_latas * 0.10
valtotalG = valor_galoes - desc_gal
valtotalL = valor_latas - desc_lat

if valtotalG < valtotalL:
    print("O valor dos galoes  é mais benefico do que latas, pois é: " , valtotalG)
    print("E o valor de latas é: " , valtotalL)

else:
    print("O valor das latas  é mais benefico do que galoes, pois é: "  , valtotalL)
    print("E o valor de galoes é: " , valtotalG)"""


#18 18. Faça um programa que calcule o tempo aproximado de download de um arquivo dado seu
#tamanho (MB) e velocidade da internet (Mbps).

tamanho = float(input("Digite o tamanho do arquivo aproximado de download de um arquivo: "))

mbps = float(input("qual a velociade de upload?"))

tempo = tamanho/mbps
tempo_min = tempo//60
tempo_hr = tempo // 3600
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60

print(f' irá demorar um total de: {tempo_hr}hr, {minutos}min, {segundos}seg')


