numero_tabuada = int(input("Digite o número que você deseja ver a tabuada: "))

print(f"\n--- Tabuada do {numero_tabuada} ---")

for multiplicador in range(1, 11):
    resultado = numero_tabuada * multiplicador
    
    print(f"{numero_tabuada} x {multiplicador} = {resultado}")


print(f"\n--- Tabuada do {numero_tabuada} ---")