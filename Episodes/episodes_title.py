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
        return text.encode('latin1').decode('utf-8')
    except UnicodeDecodeError:
        return text


# Carregar o arquivo CSV
csv_path = '../TransformedFiles/Episodes.csv'
df = pd.read_csv(csv_path)

# Decodificar entidades HTML nos títulos
df['Episode_Title'] = df['Episode_Title'].apply(decode_html_entities)

# Decodificar texto para lidar com codificação incorreta
df['Episode_Title'] = df['Episode_Title'].apply(decode_text)

# Verificar títulos com caracteres especiais
special_characters_titles = df[df['Episode_Title'].apply(has_special_characters)]['Episode_Title'].tolist()

# Imprimir títulos com caracteres especiais
for title in special_characters_titles:
    print(title)

# Atualizar a coluna Episode_Title com os títulos corrigidos
df.to_csv(csv_path, index=False, encoding='utf-8-sig')


