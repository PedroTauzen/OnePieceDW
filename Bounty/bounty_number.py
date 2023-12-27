import pandas as pd
import re
from html import unescape  # Módulo para decodificar entidades HTML


def has_special_characters(text):
    pattern = re.compile('[^a-zA-Z0-9\s]')
    return bool(pattern.search(text))


def decode_html_entities(text):
    return unescape(text)


def decode_text(text):
    try:
        # Tentar decodificar o texto usando diferentes codificações
        return text.encode('utf-8').decode('utf-8')
    except UnicodeDecodeError:
        return text


# Carregar o arquivo CSV
csv_path = '../TransformedFiles/Bounties.csv'
df = pd.read_csv(csv_path)

# Decodificar entidades HTML nos títulos
df['Character_Bounty'] = df['Character_Bounty'].apply(decode_html_entities)

# Decodificar texto para lidar com codificação incorreta
df['Character_Bounty'] = df['Character_Bounty'].apply(decode_text)

# Eliminar linhas com valor "Unknown" na coluna Character_Bounty
df = df[df['Character_Bounty'] != 'Unknown']

# Remover linhas que começam com "(" na coluna Character_Bounty
df = df[~df['Character_Name'].str.startswith('(')]

# Verificar títulos com caracteres especiais
special_characters_titles = df[df['Character_Bounty'].apply(has_special_characters)]['Character_Bounty'].tolist()

# Imprimir títulos com caracteres especiais
for title in special_characters_titles:
    print(title)

# Atualizar a coluna Episode_Title com os títulos corrigidos
df.to_csv(csv_path, index=False, encoding='utf-8-sig')


