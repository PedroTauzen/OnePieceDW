import pandas as pd

# Loading the chapters.csv file
old_characters_df = pd.read_csv('../OriginalFiles/Episodes.csv', encoding='latin1')

# Create a new dataframe
new_characters_df = old_characters_df[['episode', 'name', 'start', 'total_votes', 'average_rating']].copy()

# Rename the collumns
new_characters_df.columns = ['Episode_Number', 'Episode_Title', 'Episode_Year', 'Episode_Total_Votes',
                             'Episode_Average_Rating']

# Save the new dataframe (Chapters.csv)
new_characters_df.to_csv('../TransformedFiles/Episodes.csv', index=False)
