valor_inserido = float(input("Digite um valor numérico: "))
dobro = valor_inserido * 2
triplo = valor_inserido * 3
quadrado = valor_inserido ** 2
raiz_quadrada = valor_inserido ** (1/2) 
raiz_cubica = valor_inserido ** (1/3)

print("\n" + ("-"*25)) 
print(f"Resultados para o valor {valor_inserido}:")
print(f"1. O dobro é: {dobro}")
print(f"2. O triplo é: {triplo}")
print(f"3. O valor ao quadrado é: {quadrado}")
print(f"4. A raiz quadrada é: {raiz_quadrada:.4f}") 
print(f"5. A raiz cúbica é: {raiz_cubica:.4f}")   
print(("-")*25)