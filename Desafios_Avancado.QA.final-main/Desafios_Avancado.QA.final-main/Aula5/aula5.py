import requests

squad = [
    {
        "nome": "Ellen",
        "cep": "11630-097"
    },
    {
        "nome": "Cecilia",
        "cep": "04013-001"
    },
    {
        "nome": "Beatriz",
        "cep": "22071-020"
    },
    {
        "nome": "João",
        "cep": "40026-010"
    }
]

print("--- Cidades dos Integrantes do Squad ---")

for integrante in squad:
    cep = integrante["cep"]
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            dados_cep = response.json()
            nome = integrante["nome"]
            cidade = dados_cep.get("localidade", "Cidade não encontrada")
            
            print(f"Nome: {nome} | Cidade: {cidade}")
        else:
            print(f"Nome: {integrante['nome']} | Erro ao consultar o CEP {cep}.")

    except requests.exceptions.RequestException as e:
        print(f"Nome: {integrante['nome']} | Erro de conexão ao consultar o CEP {cep}.")