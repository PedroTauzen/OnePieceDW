import pandas as pd

# Carregar o arquivo CSV
csv_path = '../TransformedFiles/Chapters.csv'
df = pd.read_csv(csv_path)

# Limpar caracteres especiais
df['Chapter_Title'] = df['Chapter_Title'].apply(lambda x: ''.join(e for e in x if e.isalnum() or e.isspace()))

# Verificar comprimento dos títulos
df['Title_Length'] = df['Chapter_Title'].apply(len)

# Exibir títulos que podem estar causando problemas
problematic_titles = df[df['Title_Length'] > 255]['Chapter_Title']
print(problematic_titles)
