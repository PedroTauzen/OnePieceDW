import pandas as pd

# Loading the chapters.csv file
old_chapters_df = pd.read_csv('D:/Facul/IPBeja/2023-2024/1o Semestre/Sistemas de Informação/OnePiece '
                              'DataWarehouse/Python/OnePieceDW/OriginalFiles/Chapters.csv', encoding='latin1')

# Create a new dataframe
new_chapters_df = old_chapters_df[['Chapter_Number', 'Volume', 'Viz_title', 'Pages', 'Date']].copy()

# Rename the collumns
new_chapters_df.columns = ['Chapter_Number', 'Chapter_Volume', 'Chapter_Title', 'Chapter_Pages', 'Chapter_Date']

# Save the new dataframe (Chapters.csv)
new_chapters_df.to_csv('D:/Facul/IPBeja/2023-2024/1o Semestre/Sistemas de Informação/OnePiece '
                       'DataWarehouse/Python/OnePieceDW/TransformedFiles/Chapters.csv', index=False)

