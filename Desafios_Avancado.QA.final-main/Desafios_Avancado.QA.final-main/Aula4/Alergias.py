lista_frutas = ["Maçã", "Banana", "Morango", "Uva", "Abacaxi", "Kiwi"]

lista_alergias = ["Amendoim", "Lactose", "Glúten", "Camarão"]

lista_alergias.append("Morango")
lista_alergias.append("Kiwi")

print(f"Lista de Frutas: {lista_frutas}")
print(f"Lista de Alergias: {lista_alergias}")
print("--------------------------------------------------")
print("VERIFICANDO ITENS ALERGÊNICOS NA LISTA DE FRUTAS:")
print("--------------------------------------------------")

for fruta in lista_frutas:
    if fruta in lista_alergias:
        print(f"Atenção: {fruta} foi encontrado na lista de alergias!")