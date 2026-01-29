import requests
import re 

ESTADOS_FRETE_GRATIS = {
    # Norte
    'AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO',
    # Nordeste
    'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE',
    # Sul
    'RS', 'SC', 'PR',
    # Sudeste
    'SP', 'RJ', 'ES', 'MG'
}

def limpar_e_validar_cep(cep_bruto):
    """Limpa o CEP removendo caracteres não numéricos e valida o formato."""
    # Remove tudo que não for dígito (0-9)
    cep_limpo = re.sub(r'\D', '', cep_bruto)
    
    if len(cep_limpo) == 8 and cep_limpo.isdigit():
        return cep_limpo
    else:
        return None

def consultar_cep(cep):
    """Consulta a API ViaCEP e retorna os dados de localização."""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        # Lança um erro se a resposta da API for de falha (4xx ou 5xx)
        response.raise_for_status() 
        
        dados = response.json()
        
        # A API ViaCEP retorna a chave 'erro' se o CEP não for encontrado
        if dados.get('erro'):
            return None
        
        return dados

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao consultar a API: {e}")
        return None

def verificar_elegibilidade_frete(cep_dados):
    """Verifica se a UF do CEP está na lista de frete grátis."""
    if cep_dados and 'uf' in cep_dados:
        uf = cep_dados['uf']
        if uf in ESTADOS_FRETE_GRATIS:
            return True
    return False

# --- Programa Principal ---
if __name__ == "__main__":
    print("--- Loja do Joga Junto: Verificador de Frete Grátis ---")
    cep_input = input("Por favor, digite seu CEP para análise: ")

    cep_valido = limpar_e_validar_cep(cep_input)

    if not cep_valido:
        print("\n[ERRO] CEP em formato inválido. Por favor, digite um CEP com 8 dígitos.")
    else:
        print(f"\nConsultando CEP {cep_valido}...")
        dados_cep = consultar_cep(cep_valido)
        
        if not dados_cep:
            print("[ERRO] CEP não encontrado ou falha na comunicação. Verifique o número digitado.")
        else:
            cidade = dados_cep.get('localidade', 'N/A')
            uf = dados_cep.get('uf', 'N/A')
            print(f"CEP correspondente a {cidade} - {uf}.")
            
            if verificar_elegibilidade_frete(dados_cep):
                print("\n✅ Parabéns! Você tem direito a Frete Grátis!")
            else:
                print("\n❌ Poxa, seu CEP não é elegível para frete grátis.")

