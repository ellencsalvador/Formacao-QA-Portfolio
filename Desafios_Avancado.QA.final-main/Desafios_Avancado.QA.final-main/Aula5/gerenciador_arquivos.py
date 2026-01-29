import os

lista_de_tarefas = [
    "Comprar pão e leite",
    "Estudar a biblioteca OS do Python",
    "Resolver o desafio do Caique",
    "Fazer a reunião com o squad",
    "Subir o código para o GitHub"
]

nome_da_pasta = "meus_relatorios"
nome_do_arquivo = "tarefas.txt"

if not os.path.exists(nome_da_pasta):
    os.makedirs(nome_da_pasta)
    print(f"Pasta '{nome_da_pasta}' criada com sucesso!")
else:
    print(f"A pasta '{nome_da_pasta}' já existe. Nenhum diretório novo foi criado.")

caminho_completo_do_arquivo = os.path.join(nome_da_pasta, nome_do_arquivo)

with open(caminho_completo_do_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write("--- Minha Lista de Tarefas ---\n\n")     
    
    for tarefa in lista_de_tarefas:
        arquivo.write(f"- {tarefa}\n")

print(f"\nArquivo '{nome_do_arquivo}' foi salvo com sucesso dentro da pasta '{nome_da_pasta}'!")