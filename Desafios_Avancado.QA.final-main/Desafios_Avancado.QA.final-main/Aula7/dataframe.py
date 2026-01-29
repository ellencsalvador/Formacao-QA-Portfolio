import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Davi', 'Sofia', 'Lucas', 'Maria'],
    'idade': [25, 30, 22, 45, 28, 35, 29],
    'cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus']
}

df = pd.DataFrame(dados)

print("--- DataFrame Completo ---")
print(df)

moradores_recife = df[df['cidade'] == 'Recife']

print("\n--- Apenas Moradores de Recife ---")
print(moradores_recife)