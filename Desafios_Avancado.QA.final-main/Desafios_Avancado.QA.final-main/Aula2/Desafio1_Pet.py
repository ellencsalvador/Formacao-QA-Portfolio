nome_pet = input("Qual o nome do pet? ")
idade_humana = int(input(f"Qual a idade humana do(a) {nome_pet}? "))
porte_pet = input("Qual o porte do pet? (P - Pequeno, M - Médio, G - Grande): ")
quantidade_banhos = int(input(f"Quantos banhos o(a) {nome_pet} tomou nos últimos 12 meses? "))
idade_cachorro = idade_humana * 7
lucro_por_banho = 0
if porte_pet.upper() == 'G':
    lucro_por_banho = 75.00 - 20.00
elif porte_pet.upper() == 'M':
    lucro_por_banho = 60.00 - 15.00
elif porte_pet.upper() == 'P':
    lucro_por_banho = 50.00 - 5.00
else:
    print("Porte inválido. Por favor, reinicie o programa e insira P, M ou G.")
if lucro_por_banho > 0:
    lucro_total = lucro_por_banho * quantidade_banhos
if lucro_total > 0:  
    mensagem_final = f"Olá, {nome_pet} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}"
    print("\n" + ("-"*20)) 
    print(mensagem_final)
    print(("-")*20)