import pandas as pd
import re


def has_special_characters(text):
    pattern = re.compile('[^a-zA-Z0-9\s]')
    return bool(pattern.search(text))


# Carregar o arquivo CSV
csv_path = '../TransformedFiles/Chapters.csv'
df = pd.read_csv(csv_path)

# Verificar títulos com caracteres especiais
special_characters_titles = df[df['Chapter_Title'].apply(has_special_characters)]['Chapter_Title'].tolist()

# Imprimir títulos com caracteres especiais
for title in special_characters_titles:
    print(title)
