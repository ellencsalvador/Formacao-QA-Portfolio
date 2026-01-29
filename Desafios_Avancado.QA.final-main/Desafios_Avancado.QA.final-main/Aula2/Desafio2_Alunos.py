nome_aluno = input("Digite o nome do(a) aluno(a): ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

soma_das_notas = nota1 + nota2 + nota3 + nota4

media_final = soma_das_notas / 4

mensagem_output = f"Olá, {nome_aluno}! Sua média é: {media_final} pontos"

print("\n" + ("-"*20)) 
print(mensagem_output)
print(("-")*20) 