import pandas as pd

df = pd.read_csv("movies.csv", index_col="title")
recent = df                     # TODO: rows with year > 2010
print(len(recent))
ben = df                        # TODO: Ben Cole's films sorted by avg_vote, highest first
print(ben.index.tolist())

def category(x):
    return "good" if x >= 8.0 else "average"

df["category"] = "average"      # TODO: use df["avg_vote"].apply(category)
print((df["category"] == "good").sum())
