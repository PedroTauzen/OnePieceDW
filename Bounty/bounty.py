import pandas as pd

# Loading the chapters.csv file
old_characters_df = pd.read_csv('../OriginalFiles/Bounties.csv', encoding='latin1')

# Create a new dataframe
new_characters_df = old_characters_df[['Name ', 'Bounty']].copy()

# Rename the collumns
new_characters_df.columns = ['Character_Name', 'Character_Bounty']

# Save the new dataframe (Chapters.csv)
new_characters_df.to_csv('../TransformedFiles/Bounties.csv', index=False)
