import pandas as pd

df = pd.read_csv("BKN_raw.csv")
# Data Cleaning
# Remove Unecessary Columns and Rows
df = df.drop(columns=["Unnamed: 0","Lg","Tm"])

# Drop "nan" rows & columns
df = df.drop([20,41])
df = df.drop(df.columns[3], axis=1)
df = df.drop(df.columns[6], axis=1)

# Insert Season column
seasons = []
for i in range(53):
    seasons.append(2019-i)
df.insert(0, "Season", seasons)

df.to_csv("BKN_cleaned.csv")
