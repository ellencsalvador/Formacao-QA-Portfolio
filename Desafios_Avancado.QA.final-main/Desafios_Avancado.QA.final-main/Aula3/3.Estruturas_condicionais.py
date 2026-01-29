print("\n-------------------------------------------------------------")
print("-------------------------- DESAFIO IF ------------------------")
idade = int(input("Digite sua idade: "))
if idade > 18:
    print("Indivíduo possui idade mínima para dirigir")
print("--------------------------------------------------------------")

print("\n-------------------------------------------------------------")
print("------------------------ DESAFIO ELSE ------------------------")
idade = int(input("Digite sua idade: "))
if idade > 18:
    print("Indivíduo possui idade mínima para dirigir")
else:
    print("Indivíduo NÃO possui idade mínima para dirigir")
print("--------------------------------------------------------------")

print("\n-------------------------------------------------------------")
print("------------------------ DESAFIO ELIF ------------------------")
idade = int(input("Digite sua idade: "))
if idade > 18:
  print("Indivíduo possui idade mínima para dirigir")
elif idade == 17 or idade == 18:
  print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
  print("Indivíduo NÃO possui idade mínima para dirigir")
print("--------------------------------------------------------------")
