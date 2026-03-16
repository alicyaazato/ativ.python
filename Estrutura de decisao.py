#01 Faça um programa que peça dois números e imprima o maior deles.

"""
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
if num1 > num2:
    print(num1)
else:
    print(num2)
"""


#02 Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

"""
numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
print()

"""

#03 Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# • F - Feminino 
# • M - Masculino 
# • Sexo Inválido.

"""
sexo = input("Digite F para Feminino ou M para Masculino: ")
if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo == "M" or sexo == "m":
    print("Masculino")
else:
    print("Sexo Inválido")
  
"""

#04 Faça um programa que verifique se uma letra digitada é vogal ou consoante.

"""
letra = input("digite uma letra: ")  .upper

if (
    letra  == 'A' or 'a'
    or letra == 'E' or 'e'
    or letra == 'I' or 'i'
    or letra == 'U' or 'u'
    ):
    print("É uma vogal! ")

else:
    print("É uma consoante! ")

     """

# 05 Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#• A mensagem "Reprovado", se a média for menor do que sete;
#• A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
"""


#Exercício 06 Faça um programa que leia três números e mostre o maior deles.

"""
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
numero3 = float(input("Digite mais um numero: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} foi o maior numero digitado.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} foi o maior numero digitado.")
else:
    print(f"{numero3} foi o maior numero digitado.")

    """

#07 Faça um programa que leia três números e mostre o maior e o menor deles.


"""
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
num3 = float(input("Digite mais um numero: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} foi o maior numero digitado.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} foi o maior numero digitado.")
else:
    print(f"{num3} foi o maior numero digitado.")

if num1 < num2 and num1 < num3:
    print(f"{num1} foi o menor numero digitado.")
elif num2 < num1 and num2 < num3:
    print(f"{num2} foi o menor numero digitado.")
else:
    print(f"{num3} foi o menor numero digitado.")

 """


# 08 Faça um programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.


"""
preco1 = float(input("Digite o preço do produto 1: "))
preco2 = float(input("Digite o preço do produto 2: "))
preco3 = float(input("Digite o preço do produto 3: "))
if preco1 < preco2 and preco1 < preco3:
    print(f"O produto com o menor preco é o 1, custando R${preco1:.2f}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto com o menor preco é o 2, custando R${preco2:.2f}")
else:
    print(f"O produto com o menor preco é o 3, custando R${preco3:.2f}")

 """


#09 Faça um programa que leia três números e mostre-os em ordem decrescente.

"""
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite mSais um numero: "))
if n1 > n2 > n3:
    print(n1, n2, n3)

elif n1 > n3 > n2:
    print(n1, n3, n2)
elif n2 > n1 > n3:
    print(n2, n1, n3)
elif n2 > n3 > n1:
    print(n2, n3, n1)
elif n3 > n1 > n2:
    print(n3, n1, n2)
else:
    print(n3, n2, n1)
 """


# 10 Faça um programa que pergunte em que turno você estuda. Peça para digitar:
#• M - Matutino
#• V - Vespertino
#• N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
#ou "Valor Inválido!", conforme o caso 

"""
turno = input(
    "Digite seu turno, M - matutino, V - vespertino, N - noturno: "
).upper()
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")

"""

#Exercício 11 As Organizações Tabajara resolveram dar um aumento de salário aos seus 
# colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. 
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte 
# critério, baseado no salário atual:

#• salários até R$ 280,00 (incluindo) : aumento de 20%

#• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%

#• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%

#• salários de R$ 1500,00 em diante : aumento de 5%

#Após o aumento ser realizado, informe na tela:

#• o salário antes do reajuste;

#• o percentual de aumento aplicado;

#• o valor do aumento;

#• o novo salário, após o aumento.


"""

salario_anterior = float(input("Digite seu salário atual: "))
salario_atual = 0.0
diferenca_entre_salarios = 0.0
percentual_de_aumento = 0.0

if salario_anterior <= 280:
    percentual_de_aumento = 20
elif salario_anterior <= 750:
    percentual_de_aumento = 15
elif salario_anterior <= 1500:
    percentual_de_aumento = 10
else:
    percentual_de_aumento = 5

diferenca_entre_salarios = salario_anterior * (percentual_de_aumento / 100)
salario_atual = salario_anterior + diferenca_entre_salarios
print(f"Seu salário antes do reajuste era de R${salario_anterior:.2f}")
print(f"Seu salário foi aumentado em {percentual_de_aumento}%")
print(f"Seu salário foi aumentado em R${diferenca_entre_salarios:.2f}")
print(f"Seu salário atual é de R${salario_atual:.2f}")

"""
#12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são 
# do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o 
# Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#• Salário Bruto até 900 (inclusive) - isento
#• Salário Bruto até 1500 (inclusive) - desconto de 5%
#• Salário Bruto até 2500 (inclusive) - desconto de 10%
#• Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora 
# é 5 e a quantidade de hora é 220.
#• Salário Bruto: (5 * 220) : R$ 1100,00
#• (-) IR (5%) : R$ 55,00
#• (-) INSS ( 10%) : R$ 110,00
#• FGTS (11%) : R$ 121,00

#• Total de descontos : R$ 165,00
#• Salário Liquido : R$ 935,00


"""
valor_da_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = valor_da_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = salario_bruto * (desconto_ir / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11 / 100)
total_de_descontos = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(
    f"\nSalário Bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${total_de_descontos:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)

"""

#13 Faça um programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
dia_int = int(input("Digite o número do dia da semana: "))
dia_str = ""
if dia_int == 1:
    dia_str = "Domingo"
elif dia_int == 2:
    dia_str = "Segunda"
elif dia_int == 3:
    dia_str = "Terça"
elif dia_int == 4:
    dia_str = "Quarta"
elif dia_int == 5:
    dia_str = "Quinta"
elif dia_int == 6:
    dia_str = "Sexta"
elif dia_int == 7:
    dia_str = "Sábado"

if dia_str == "":
    print("Valor inválido")
else:
    print(f"O dia correspondente é {dia_str}")

"""

#14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à 
# tabela abaixo:
#• Entre 9.0 e 10.0 -> A
#• Entre 7.5 e 9.0 -> B
#• Entre 6.0 e 7.5 -> C
#• Entre 4.0 e 6.0 -> D
#• Entre 4.0 e zero -> E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


"""
nota1 = float(input("Digite a primeira nota do semestre: "))
nota2 = float(input("Digite a segunda nota do semestre: "))

media = (nota1 + nota2) / 2

if media >= 9:
    aproveitamento = "A"
elif media >= 7.5:
    aproveitamento = "B"
elif media >= 6:
    aproveitamento = "C"
elif media >= 4:
    aproveitamento = "D"
else:
    aproveitamento = "E"

if aproveitamento == "D" or aproveitamento == "E":
    print(f"REPROVADO\nAproveitamento: {aproveitamento}")
else:
    print(f"APROVADO\nAproveitamento: {aproveitamento}")
"""





#15 Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os
# valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: 
# equilátero, isósceles ou escaleno.
#• Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#• Triângulo Equilátero: três lados iguais;
#• Triângulo Isósceles: quaisquer dois lados iguais;
#• Triângulo Escaleno: três lados diferentes;

"""

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (
    (lado1 + lado2 > lado3)
    and (lado1 + lado3 > lado2)
    and (lado2 + lado3 > lado1)
):
    if (lado1 == lado2) and (lado2 == lado3):
        print("É um triângulo equilátero!")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("É um triângulo isósceles!")
    else:
        print("É um triângulo escaleno!")
else:
    print("Não é um triângulo!")

"""

# 16 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
# nas seguintes situações:
#• Se o usuário informar o valor de A igual a zero, a equação não é do segundo
#grau e o programa não deve pedir os demais valores, sendo encerrado;
#• Se o delta calculado for negativo, a equação não possui raízes reais.
#Informe ao usuário e encerre o programa;


#• Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
#informe-a ao usuário;
#• Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;

"""

a = float(input("Digite o valor de a: "))
if a == 0:
    print("Não é uma equação do segundo grau")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Delta menor que 0. Não há raízes reais.")
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print(f"Delta é zero. A raíz é {raiz}")
    else:
        raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
        raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)
        print(
            f"Delta maior que zero. A raíz 1 é {raiz1}, e a raiz 2 é {raiz2}"
        )

"""



# 17 Faça um programa que peça um número correspondente a um determinado ano e em seguida 
# informe se este ano é ou não bissexto.

"""

ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")

"""

#18 Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma 
# data válida.

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



# 19 Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de 
# centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da 
# vírgula entre outros. Exemplo:
#• 326 = 3 centenas, 2 dezenas e 6 unidades
#• 12 = 1 dezena e 2 unidades

"""
import math
numero = int(input("Digite um número menor ou igual a 1000: "))
if numero <= 1000:
    centena = numero / 100
    centena2 = math.floor(float(centena))
    resto_centena = centena - centena2
    resto_multiplicado = resto_centena * 100

    dezena = resto_multiplicado / 10
    dezena2 = math.floor(float(dezena))
    unidade = dezena - dezena2
    unidade_certo = unidade * 10

    print("Centena(s): ", centena2)
    print("dezena(s): ", dezena2)
    print("Unidade(s): ", round(unidade_certo))

else:
    print("VOCÊ DIGITOU UM NÚMERO MAIOR QUE 1000")

"""


#20 Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular 
# a média alcançada por aluno e apresentar:
#• A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#• A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#• A mensagem "Aprovado com Distinção", se a média for igual a 10.

"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("APROVADO")
elif media < 7:
    print("REPROVADO")
else:
    print("APROVADO com DISTINÇÃO")

    """

#21 Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor 
# do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis 
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#• Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma 
# nota de 50, uma nota de 5 e uma nota de 1;
#• Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma 
# nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""


import math
saque = int(input("Valor para sacar: "))
nota100 = saque / 100
nota100_certo = math.floor(nota100)
resto_nota_100 = (nota100 - nota100_certo) * 100

nota50 = resto_nota_100 / 50
nota50_certo = math.floor(nota50)
resto_nota_50 = (nota50 - nota50_certo) * 50

nota10 = resto_nota_50 / 10
nota10_certo = math.floor(nota10)
resto_nota_10 = (nota10 - nota10_certo) * 10

nota5 = resto_nota_10 / 5
nota5_certo = math.floor(nota5)
nota1 = (nota5 - nota5_certo) * 5

print("Notas 100: ", nota100_certo, "\nNotas50: ", nota50_certo, "\nNota 10: ", nota10_certo, "\nNota 1: ", round(nota1))

"""





#22 Faça um programa que peça um número inteiro e determine se ele é par ou ímpar. 
# Dica: utilize o operador módulo (resto da divisão).

"""
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
    
    
"""



#23 Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: 
# utilize uma função de arredondamento.


"""
numero = float(input("Digite um número: "))
if numero % 1 == 0:
    print("Inteiro")
else:
    print("Decimal")

    
"""


#24 Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele 
# deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o 
# número é:
#• par ou ímpar;
#• positivo ou negativo;
#• inteiro ou decimal.

"""

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")


def checar():
    if (resultado_operacao // 1 == resultado_operacao):
        print("Inteiro")
        if resultado_operacao % 2 == 0:
            print("Par")
            if resultado_operacao > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")
    else:
        print("Decimal")


if operacao == '+':
    resultado_operacao = numero1 + numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '-':
    resultado_operacao = numero1 - numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '/':
    resultado_operacao = numero1 / numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '*':
    resultado_operacao = numero1 * numero2
    print("Resultado: ", resultado_operacao)
    checar()
else:
    print("Valor Invalido")

"""


#25 Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#1. "Telefonou para a vítima?"
#2. "Esteve no local do crime?"
#3. "Mora perto da vítima?"
#4. "Devia para a vítima?"
#5. "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
# como "Inocente".

"""
perguntas = [
    "Telefonou para a vítima?: ",
    "Esteve no local do crime?: ",
    "Mora perto da vítima?: ",
    "Devia para a vítima?: ",
    "Já trabalhou com a vítima?: "
]
resposta = 0

for status in perguntas:
    resposta += (input(status) == "sim")

if resposta == 5:
    print("Assassino")

elif resposta >= 3:
    print("Cúmplice")

elif resposta == 2:
    print("Suspeito")

else:
    print("Inocente")

"""


# 26 Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#• Álcool:
#o até 20 litros: desconto de 3% por litro
#o acima de 20 litros: desconto de 5% por litro
#• Gasolina:
#o até 20 litros: desconto de 4% por litro
#o acima de 20 litros: desconto de 6% por litro

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado 
# da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo 
# cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o preço do litro do 
# álcool é R$ 1,90.



"""

litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preco = 0
if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100
    else:
        preco -= 1.9 * litros * 5 / 100
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100
    else:
        preco -= 2.5 * litros * 6 / 100
print(f"O preço a pagar é R${preco:.2f}")


"""



#27 Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#• Morango: Até 5 Kg -> R$ 2,50 por Kg | Acima de 5 Kg -> R$ 2,20 por Kg
#• Maçã: Até 5 Kg -> R$ 1,80 por Kg | Acima de 5 Kg -> R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a 
# quantidade (em Kg) de morangos e a quantidade (em Kg) de açãs adquiridas e escreva o valor 
# a ser pago pelo cliente.

"""

if morango <= 5:
    valor += morango * 2.5
else:
    valor += morango * 2.2
if maca <= 5:
    valor += maca * 1.8
else:
    valor += maca * 1.5

if (morango + maca) > 8 or valor > 25:
    valor -= valor * 10 / 100

print(f"O valor a ser pago é R${valor:.2f}")

"""


#28 O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#• File Duplo: Até 5 Kg -> R$ 4,90 por Kg | Acima de 5 Kg -> R$ 5,80 por Kg
#• Alcatra: Até 5 Kg -> R$ 5,90 por Kg | Acima de 5 Kg -> R$ 6,80 por Kg
#• Picanha: Até 5 Kg -> R$ 6,90 por Kg | Acima de 5 Kg -> R$ 7,80 por Kg

#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da 
# promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for 
# feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e 
# gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, 
# preço total, tipo de pagamento, valor do desconto e valor a pagar.

"""
carne = input("Digite F para filé duplo, A para alcatra e P para picanha: ")
peso = float(input("Digite quantos quilos dessa carne vai comprar: "))
pagamento = input("Dinheiro ou cartão tabajara (5% de desconto)? D ou C: ")
preco_total = 0

print("\nHipermercado Tabajara\nCupom fiscal\n")
if carne == "F" or carne == "f":
    print("Item: Filé Duplo")
    if peso > 5:
        preco_total = peso * 5.8
    else:
        preco_total = peso * 4.9
elif carne == "A" or carne == "a":
    print("Item: Alcatra")
    if peso > 5:
        preco_total = peso * 6.8
    else:
        preco_total = peso * 5.9
elif carne == "P" or carne == "p":
    print("Item: Picanha")
    if peso > 5:
        preco_total = peso * 7.8
    else:
        preco_total = peso * 6.9
print(f"Quantidade: {peso:.2f}Kg")
print(f"Preço total: R${preco_total:.2f}")
if pagamento == "D" or pagamento == "d":
    print("Tipo de pagamento: Dinheiro")
    desconto = 0
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")
elif pagamento == "C" or pagamento == "c":
    print("Tipo de pagamento: Cartão Tabajara")
    desconto = preco_total * 5 / 100
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")


"""

