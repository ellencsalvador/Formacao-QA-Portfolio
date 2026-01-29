def verificar_paridade(numero_matricula):
    """
    Esta função recebe um número inteiro e verifica se ele é par ou ímpar.
    Ela retorna a string "par" ou "ímpar".
    """
    if numero_matricula % 2 == 0:
        return "par"
    else:
        return "ímpar"

lista_matriculas = []

print("--- SISTEMA DE CADASTRO DA OLIMPÍADA ---")
print("Por favor, insira os 5 próximos números de matrícula.")

while len(lista_matriculas) < 5:
    try:
        matricula = int(input(f"Digite a {len(lista_matriculas) + 1}ª matrícula: "))
        
        lista_matriculas.append(matricula)
        
    except ValueError:
        print("Erro: Por favor, digite apenas números.")

print("\n--- PROCESSANDO A DIVISÃO DOS TIMES ---")

for matricula_atual in lista_matriculas:
    
    resultado = verificar_paridade(matricula_atual)
    
    if resultado == "par":
        print(f"Matrícula {matricula_atual}: VOCÊ ESTÁ NO TIME AZUL")
    else:
        print(f"Matrícula {matricula_atual}: VOCÊ ESTÁ NO TIME AMARELO")

print("\n--- Processamento finalizado! ---")