import pandas as pd

df = pd.read_csv("movies.csv")
print(df.shape)
missing = 0              # TODO: df["language"].isnull().sum()
print(missing)
clean = df               # TODO: drop rows with missing values
print(clean.shape)
print(round(0, 2))       # TODO: mean of avg_vote
