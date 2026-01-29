valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra > 500:
    print("\nPARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")

elif valor_compra >= 250:
    print("\nPARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")

else:
    print("\nPOXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")

print("--------------------------------------------------------------")