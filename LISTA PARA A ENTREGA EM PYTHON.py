#Exercicio 1)

print("------BOLETIM DE NOTAS------\n")
nome = str(input("Digite o nome do aluno: "))
disciplina = str(input("Digite qual a disciplina: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
status = str
print(f"A media do aluno é: {media}\n")
if media >= 0 and media <= 39:
         status = "Reprovado"
elif media >= 40 and media <= 59:
        status = "Recuperação"
elif media >= 60 and media <= 100:
        status = "Aprovado"
elif media > 100:
        status = "A media excede o limite de nota"
print("---RELATÓRIO---\n")
print(f"Aluno: {nome}\n")
print("Curso: Engenharia de Software\n")
print("Semestre: Segundo\n")
print(f"Disciplina: {disciplina}\n")
print(f"Status: {status}\n")

#Exercicio 2)

a =int(input("Escreva um número= "))
b =int(input("Escreva um outro número= "))

soma = a+b
print("A soma entre {} e {} tem valor de= {}".format(a,b,soma))

#Exercicio 3)

a =int(input("Escreva um número= "))
b =int(input("Escreva um outro número= "))

sub = a-b
print("A subtração entre {} e {} tem valor de= {}".format(a,b,sub))

#Exercicio 4)

a =int(input("Escreva um número= "))
b =int(input("Escreva um outro número= "))

mult = a*b
print("A multiplicação entre {} e {} tem valor de= {}".format(a,b,mult))

#Exercicio 5)

a =int(input("Escreva um número= "))
b =int(input("Escreva um outro número= "))

div = a/3

print("A divisão entre {} e {} tem valor de= {}".format(a,b,div))

#Exercicio 6)

print("Dobro ou triplo \n")
print("\n")

a = int(input("Escreva um número= "))

print("O dobro do núemro {} tem valor de= {} \n e o triplo dele tem valor de= {}".format(a,a*2,a*3))

#Exercicio 7)

print("Vamos ver qual é o antecessor e o sucessor de um número! \n")
print("\n")

a = int(input("Escreva um número= "))

print("O antecessor do núemro {} tem valor de= {} \n e o sucessor dele tem valor de= {}".format(a,a-1,a+1))


#Exercicio 8)

alturat = float(input("Digite a altura do triângulo: "))
baset = float(input("Digite a base do triangulo: "))

areat = float((alturat*baset) / 2)

print(f"A área do triângulo é: {areat}\n")

#Exercicio 9)

lado1 = float(input("Digite o primeiro lado do retângulo: "))
lado2 = float(input("Digite o segundo lado do retângulo: "))

perimetro = float((lado1*2) +(lado2*2))

print(f"O perímetro do retângulo é: {perimetro}\n")
print("--------------------------")

#Exercicio 10)

#Positivo ou Negativo

a = float(input("Digite um valor: "))

if (a > 0):
    print("O numero é POSITIVO!")
elif (a == 0):
    print("O numero é igual a ZERO!")
elif (a < 0):
    print("O numero é NEGATIVO!")

#Exercicio 11)

#Impar ou Par

b = float(input("Digite um valor: "))

if (b % 2 == 0):
    print("O numero é PAR!")
elif (b % 2 == 1):
    print("O numero é IMPAR!")

#Exercicio 12)

#Qual é maior? (2 Variaveis)

c = float(input("Digite um valor: "))
d = float(input("Digite um segundo valor: "))

if (c > d):
    print(f"{c} é maior que {d}")
elif (c == d):
    print("Os valores são iguais!")
elif (c < d):
    print(f"{d} é maior que {c}")

#Exercicio 13)

#Qual é maior? (3 Variaveis)

e = float (input("Digite um valor: "))
f = float(input("Digite um segundo valor: "))
g = float(input("Digite um terceiro valor: "))

if (e > f) and (e > g):
    print(f"{e} é maior que {f} e {g}")
elif (f > e) and (f > g):
    print(f"{f} é maior que {g} e {e}")
elif (g > f) and (g > e):
    print(f"{g} é maior que {f} e {e}")

#Exercicio 14)

idade = int(input("Qual a sua idade?\n "))
titulo = int(input("Digite 1 se você possui titulo de eleitor e 0 se você nao possui\n "))

if idade >= 18 and titulo == 1:
    print("Você pode votar!")
else:
    print("Você não pode votar!")

#Exercicio 15)

idade = int(input("Qual a sua idade?\n "))
carteira = int(input("Digite 1 se você possui cnh e 0 se você nao possui\n "))

if idade >= 18 and carteira == 1:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")

#Exercicio 16)

valor = float(input("Qual o valor de compra?\n "))
forma = str(input("Qual a forma de compra? (avista ou aprazo) \n"))

desconto = valor * 0.10
valord = valor - desconto

if forma == "avista":
    print("O valor avista inclue 10% de desconto, assim saindo por {}".format(valord))
else:
    print("O valor a prazo é : {}".format(valor))

#Exercicio 17)

print("EVENTO!\n")

idade = int(input("Qual a sua idade? \n"))
ingresso = str(input("Você tem  ingresso para o evento? \n"))

if ingresso == "Sim" and idade >= 18 or ingresso == "sim" and idade <= 18:
    print("Você pode entrar no evento!")
else:
    print("Você não pode entrar no evento!")

#Exercicio 18)

print("Intervalo 10 a 50\n")

n = float(input("Digite um numero: \n"))

if n >= 10 and n <= 50:
    print("O numero digitado esta entre 10 e 50!")
else:
    print("O numero digitado não esta entre 10 e 50!")

#Exercicio 19)

print("Cadastro e autenticação!\n")

cadastro = str(input("Qual o nome do cadastro? \n"))
senha = int(input("Qual a senha do cadastro? \n"))

print("Agora faremos o Login!\n")

login = str(input("Qual o login? \n"))
if cadastro == login:
    senhal = int(input("Qual a senha? \n"))
    if senha == senhal:
        print("Login com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Login incorreto!")

#Exercicio 20)


print("Calculadora Simples/n")

a = float (input("Insira um numero: "))
b = float (input("Insira um segundo numero: "))
operador = str(input("Insira um operador: "))

if operador == "+":
    print(a+b)
if operador == "-":
    print(a-b)
if operador == "*":
    print(a*b)
if operador == "/":
    if b != 0:
        print(a/b)
    else:
        print("Esta divisão não existe")

#Exercicio 21)

print("Prática Esportiva\n")

idade = int(input("Informe sua idade: "))

if idade >= 12 and idade <= 18:
    autorizacao = str(input("Você possui autorização?\n"))
    if autorizacao == "sim" or autorizacao == "Sim":
        print("Você pode fazer parte da pratica esportiva")
    else:
        print("Você não pode fazer parte da pratica esportiva")
else:
    print ("Você não tem a idade esperada no escopo!")

#Exercício 22)

podesair = str(input("Esta chovendo? \n"))
if podesair.lower() == "nao":
    podesair = "Pode sair"
    print(podesair)
else:
    podesair = "Não pode sair"
    print(podesair)

#Exercicio 23)

idade = int(input("Qual a sua idade? "))

if idade < 12:
    print("Você é uma criança!")
if idade >= 12 and idade < 18:
    print("Você é um adolescente!")
if idade >= 18 and idade <50:
    print("Você é um adulto!")
if idade >= 50:
    print("Você é idoso!")

#Exercicio 24)

print("Escolha entre PIX / Crédito / Debito")
forma = str(input("Digite a forma de pagamento: "))
if forma == "PIX":
    print("Escaneie o QR CODE a seguir: \n")
    print("Pagamento realizado em PIX")
if forma == "Crédito":
    print("Pagamento realizado em crédito ")
if forma == "Debito":
    print("Pagamento realizado em debito ")

#Exercicio 25)

preco = float(input("Digite o preço do produto: "))

if preco >= 100 and preco < 300:
    preco = preco * 0.9
    print(f"Você tem 10% de desconto e o produto custa: {preco}")
elif preco >= 300 and preco <= 500:
    preco = preco * 0.85
    print(f"Você tem 15% de desconto e o produto custa: {preco}")
elif preco >= 500:
    print(f"Você tem 20% de desconto e o produto custa: {preco}")
else:
    print(f"O produto não tem desconto e custa {preco}")

#Exercicio 26)

print("Calculador de salario\n")

salario = float(input("Digite seu salario: "))

print(f"Seu salario antes do aumento e: {salario}\n")

if salario <= 2000:
    salario = salario * 1.15
    salario_rounded = round(salario, 2)
    print(f"Seu salario apos o aumento e: {salario_rounded}\n")
else:
    print("Voce nao recebeu aumento\n")

#Exercicio 27)

print("Vamos descobrir a natureza do triângulo!! \n")


a = int(input("Escreva o lado A do triângulo= "))
b = int(input("Escreva o lado B do triângulo= "))
c = int(input("Escreva o lado C do triângulo= "))

if a == b == c:
  print("O triângulo é equilátero")
elif a == b or a == c or b == c:
  print("O triângulo é isóceles")
else:
  print("O triângulo é escaleno")

