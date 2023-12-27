import pandas as pd

# Loading the chapters.csv file
old_characters_df = pd.read_csv('../OriginalFiles/Characters.csv', encoding='latin1')

# Create a new dataframe
new_characters_df = old_characters_df[['name', 'chapter', 'episode', 'year']].copy()

# Rename the collumns
new_characters_df.columns = ['Character_Name', 'Chapter_Number', 'Episode_Number', 'Character_Appearance_Year']

# Save the new dataframe (Chapters.csv)
new_characters_df.to_csv('../TransformedFiles/Characters.csv', index=False)
