print("--- Imprimindo todos os números de 1 a 1000 ---")

for numero in range(1, 1001):
    print(numero)

print("\n--- Imprimindo APENAS os números pares de 1 a 1000 ---")

for numero in range(1, 1001):
    if numero % 2 == 0:
      print(numero)
