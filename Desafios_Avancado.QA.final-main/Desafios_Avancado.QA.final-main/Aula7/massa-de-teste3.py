# Passo 1: Importar as bibliotecas necessárias
from faker import Faker
import csv
import pandas as pd
from datetime import date

# Passo 2: Inicializar o Faker para gerar dados em português
fake = Faker('pt_BR')

def gerar_massa_de_dados(num_pessoas=15):
    """
    Cria uma lista de dicionários com dados falsos de pessoas.
    Cada dicionário representa uma pessoa com nome, idade e cidade.
    """
    lista_de_pessoas = []
    ano_atual = date.today().year

    print(f"Gerando dados para {num_pessoas} pessoas...")
    
    for _ in range(num_pessoas):
        # Gera uma data de nascimento para calcular a idade de forma realista
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=70)
        
        pessoa = {
            'nome': fake.name(),
            'idade': ano_atual - data_nascimento.year,
            'cidade': fake.city()
        }
        lista_de_pessoas.append(pessoa)
        
    print("Dados gerados com sucesso!")
    return lista_de_pessoas

def salvar_em_csv(lista_de_pessoas, nome_arquivo):
    """
    Salva uma lista de dicionários em um arquivo no formato CSV.
    """
    # Verifica se a lista não está vazia para evitar erros
    if not lista_de_pessoas:
        print("A lista de pessoas está vazia. Nenhum arquivo foi criado.")
        return

    # Pega os nomes das colunas a partir das chaves do primeiro dicionário
    colunas = lista_de_pessoas[0].keys()

    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # DictWriter é ideal para escrever dicionários em CSV
            writer = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            
            # Escreve o cabeçalho (nome, idade, cidade)
            writer.writeheader()
            
            # Escreve todas as linhas da lista de pessoas
            writer.writerows(lista_de_pessoas)
            
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

    except IOError as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

# --- Execução Principal do Script ---

# Define o nome do arquivo que será gerado
arquivo_de_saida = 'massa_de_teste_pessoas.csv'

# 1. Gera a massa de dados
pessoas_geradas = gerar_massa_de_dados(num_pessoas=20)

# 2. Salva os dados gerados no arquivo CSV
salvar_em_csv(pessoas_geradas, arquivo_de_saida)

# 3. Usa o Pandas para ler e analisar o arquivo que acabamos de criar
print("\n--- Análise com Pandas ---")
try:
    # Lê o arquivo CSV para um DataFrame
    df = pd.read_csv(arquivo_de_saida)

    # Exibe o DataFrame completo
    print("DataFrame completo lido do arquivo CSV:\n")
    print(df)
    
    # Exemplo de filtro: Exibir apenas pessoas com 30 anos ou mais
    pessoas_acima_de_30 = df[df['idade'] >= 30]
    print("\nFiltro: Pessoas com 30 anos ou mais:\n")
    print(pessoas_acima_de_30)

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_de_saida}' não foi encontrado para leitura.")