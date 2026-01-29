minha_tupla = ("banana", "maçã", "laranja", "uva", "morango")

print("\n-------------------------------------------------------------")
print("------------------------- MINHA TUPLA ------------------------")
print("--------------------------------------------------------------")
print(f"1. Tupla original: {minha_tupla}")

minha_lista = list(minha_tupla)
print("\n-------------------------------------------------------------")
print("-------------------- LISTA DA MINHA TUPLA --------------------")
print("--------------------------------------------------------------")
print(f"2. Tupla convertida para lista: {minha_lista}")

minha_lista.append("abacaxi")
minha_lista.append("melancia")
print("\n-------------------------------------------------------------")
print("----------- LISTA DE NOVOS DADOS DA MINHA TUPLA --------------")
print("--------------------------------------------------------------")
print(f"3. Lista com 2 novos dados: {minha_lista}")

minha_lista.pop(0)
print("\n-------------------------------------------------------------")
print("----------- LISTA APÓS REMOVER O PRIMEIRO DADO ---------------")
print("--------------------------------------------------------------")
print(f"4. Lista após remover o primeiro dado: {minha_lista}")

minha_lista.pop()
print("\n-------------------------------------------------------------")
print("------------ LISTA APÓS REMOVER O PRIMEIRO DADO --------------")
print("--------------------------------------------------------------")
print(f"5. Lista após remover o último dado: {minha_lista}")

primeiro_dado = minha_lista[0]
print("\n-------------------------------------------------------------")
print("--------------- PRIMEIRO DADO DA LISTA ATUAL -----------------")
print("--------------------------------------------------------------")
print(f"6. O primeiro dado da lista atual é: {primeiro_dado}")

quantidade_dados = len(minha_lista)
print("\n-------------------------------------------------------------")
print("------------ QUANTIDADE DE DADOS DA MINHA LISTA --------------")
print("--------------------------------------------------------------")
print(f"7. A quantidade de dados na lista é: {quantidade_dados}")

dados_pessoais = {
    "Nome": "Ellen Salvador",
    "Idade": 43,
    "Profissão": "Desenvolvedora"
}
print("\n-------------------------------------------------------------")
print("--------------------- DICIONÁRIO CRIADO ----------------------")
print("--------------------------------------------------------------")
print(f"8. Dicionário criado: {dados_pessoais}")

nome_no_dicionario = dados_pessoais["Nome"]
print("\n-------------------------------------------------------------")
print("------------------- NOME DO DICIONÁRIO -----------------------")
print("--------------------------------------------------------------")
print(f"9. O valor da chave 'Nome' é: {nome_no_dicionario}")
