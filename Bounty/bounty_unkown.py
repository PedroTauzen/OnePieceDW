import pandas as pd

# Carregar o arquivo CSV
csv_path = 'seu_arquivo.csv'
df = pd.read_csv(csv_path)

# Eliminar linhas com valor "Unknown" na coluna Character_Bounty
df = df[df['Character_Bounty'] != 'Unknown']

# Salvar o DataFrame de volta no arquivo CSV
df.to_csv(csv_path, index=False)
