import pandas as pd

# Carregar o DataFrame do arquivo CSV
df = pd.read_csv('D:/Facul/IPBeja/2023-2024/1o Semestre/Sistemas de Informação/OnePiece '
                 'DataWarehouse/Python/OnePieceDW/TransformedFiles/Chapters.csv')

# Converter a coluna Chapter_Date para o formato de data padrão do SQL Server (sem tempo)
df['Chapter_Date'] = pd.to_datetime(df['Chapter_Date']).dt.strftime('%Y-%m-%d')

# Exibir o DataFrame atualizado
print(df)

# Salvar o DataFrame de volta no arquivo CSV
df.to_csv('D:/Facul/IPBeja/2023-2024/1o Semestre/Sistemas de Informação/OnePiece '
          'DataWarehouse/Python/OnePieceDW/TransformedFiles/Chapters.csv', index=False)
