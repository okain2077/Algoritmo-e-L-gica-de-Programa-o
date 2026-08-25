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

a = float(input("Digite um numero: "))
b = float(input("Digite um segundo numero: "))

soma = float(a+b)
sub = float(a-b)
mult = float(a*b)
div = float(a/b)

print("------------------------------\n")
print(f"A soma é : {soma}\n")
print("------------------------------\n")
print(f"A subtração é: {sub}\n")
print("------------------------------\n")
print(f"A multiplicação é: {mult}\n")
print("------------------------------\n")
print(f"A divisão é: {div}")
print("------------------------------")

Exercicio 3)

c = float(input("Digite um numero: "))

dobro = float(c*2)
triplo = float(c*3)
ant = float(c-1)
suc = float(c+1)

print("--------------------------\n")
print(f"O dobro é: {dobro}\n")
print("--------------------------\n")
print(f"O triplo é: {triplo}\n")
print("--------------------------\n")
print(f"O antecessor é: {ant}\n")
print("--------------------------\n")
print(f"O sucessor é: {suc}")
print("--------------------------")

#Exercicio 4)

alturat = float(input("Digite a altura do triângulo: "))
baset = float(input("Digite a base do triangulo: "))

areat = float((alturat*baset) / 2)

print(f"A área do triângulo é: {areat}\n")

#Exercicio 5)

lado1 = float(input("Digite o primeiro lado do retângulo: "))
lado2 = float(input("Digite o segundo lado do retângulo: "))

perimetro = float((lado1*2) +(lado2*2))

print(f"O perímetro do retângulo é: {perimetro}\n")
print("--------------------------")

#Exercicio 6)

#Positivo ou Negativo

a = float(input("Digite um valor: "))

if (a > 0):
    print("O numero é POSITIVO!")
elif (a == 0):
    print("O numero é igual a ZERO!")
elif (a < 0):
    print("O numero é NEGATIVO!")

#Exercicio 7)

#Impar ou Par

b = float(input("Digite um valor: "))

if (b % 2 == 0):
    print("O numero é PAR!")
elif (b % 2 == 1):
    print("O numero é IMPAR!")

#Exercicio 8)

#Qual é maior? (2 Variaveis)

c = float(input("Digite um valor: "))
d = float(input("Digite um segundo valor: "))

if (c > d):
    print(f"{c} é maior que {d}")
elif (c == d):
    print("Os valores são iguais!")
elif (c < d):
    print(f"{d} é maior que {c}")

#Exercicio 9)

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

#Exercicio 10)

idade = int(input("Qual a sua idade?\n "))
titulo = int(input("Digite 1 se você possui titulo de eleitor e 0 se você nao possui\n "))

if idade >= 18 and titulo == 1:
    print("Você pode votar!")
else:
    print("Você não pode votar!")

#Exercicio 11)

idade = int(input("Qual a sua idade?\n "))
carteira = int(input("Digite 1 se você possui cnh e 0 se você nao possui\n "))

if idade >= 18 and carteira == 1:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")

#Exercicio 12)

valor = float(input("Qual o valor de compra?\n "))
forma = str(input("Qual a forma de compra? (avista ou aprazo) \n"))

desconto = valor * 0.10
valord = valor - desconto

if forma == "avista":
    print("O valor avista inclue 10% de desconto, assim saindo por {}".format(valord))
else:
    print("O valor a prazo é : {}".format(valor))

#Exercicio 13)

print("EVENTO!\n")

idade = int(input("Qual a sua idade? \n"))
ingresso = str(input("Você tem  ingresso para o evento? \n"))

if ingresso == "Sim" and idade >= 18 or ingresso == "sim" and idade <= 18:
    print("Você pode entrar no evento!")
else:
    print("Você não pode entrar no evento!")

#Exercicio 14)


#Exercicio 2
print("Intervalo 10 a 50\n")

n = float(input("Digite um numero: \n"))

if n >= 10 and n <= 50:
    print("O numero digitado esta entre 10 e 50!")
else:
    print("O numero digitado não esta entre 10 e 50!")

#Exercicio 15)

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
