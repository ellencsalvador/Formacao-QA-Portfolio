def verificar_paridade(numero_matricula):
    
    if numero_matricula % 2 == 0:
        return "par"
    else:
        return "ímpar"

print("--- BEM-VINDO(A) À OLIMPÍADA DO CONHECIMENTO ---")

matricula_aluno = int(input("Por favor, digite o número da sua matrícula: "))

resultado = verificar_paridade(matricula_aluno)

if resultado == "par":
    print("\nVOCÊ ESTÁ NO TIME AZUL")
else:
    print("\nVOCÊ ESTÁ NO TIME AMARELO")