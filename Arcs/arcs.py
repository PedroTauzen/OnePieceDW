import pandas as pd

# Loading the chapters.csv file
old_characters_df = pd.read_csv('../OriginalFiles/Arcs.csv', encoding='latin1')

# Create a new dataframe
new_characters_df = old_characters_df[['Arc', 'Start onChapter', 'TotalChapters', 'TotalPages', 'Start onEpisode',
                                       'TotalEpisodes', 'TotalMinutes(avg 24)']].copy()

# Rename the collumns
new_characters_df.columns = ['Arc_Name', 'Arc_Chapter_Start', 'Arc_Total_Chapters', 'Arc_Total_Pages',
                             'Arc_Episode_Start', 'Arc_Total_Episodes', 'Arc_Total_Minutes']

# Save the new dataframe (Chapters.csv)
new_characters_df.to_csv('../TransformedFiles/Arcs.csv', index=False)
