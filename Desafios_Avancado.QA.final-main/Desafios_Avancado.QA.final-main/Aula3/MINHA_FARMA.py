valor_total_compra = float(input("Digite o valor total da compra do cliente: R$ "))

print("\n----------------------------------------")
print("------- MENSAGEM NO CUPOM FISCAL -------")
print("----------------------------------------")

if valor_total_compra >= 100:
    print("SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO.")
else:
    print("OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE R$10 REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?")

print("-------------------------------------")