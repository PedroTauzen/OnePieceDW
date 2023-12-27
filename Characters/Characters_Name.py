import pandas as pd
import re


def has_special_characters(text):
    pattern = re.compile('[^a-zA-Z0-9\s]')
    return bool(pattern.search(text))


# Carregar o arquivo CSV
csv_path = '../TransformedFiles/Characters.csv'
df = pd.read_csv(csv_path)

# Verificar títulos com caracteres especiais
special_characters_titles = df[df['Character_Name'].apply(has_special_characters)]['Character_Name'].tolist()

# Imprimir títulos com caracteres especiais
for title in special_characters_titles:
    print(title)
