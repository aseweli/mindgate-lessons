## Why it matters

Questions about data are selections: "films by Ana Ruiz rated above 8", "the 5 longest films". This lesson is the
syllabus topic *querying and complex selection*.

## 1. Columns

```python
import pandas as pd

df = pd.read_csv("movies.csv", index_col="title")
print(type(df["year"]).__name__, type(df[["year"]]).__name__)
print(df[["director", "avg_vote"]].head(2))
```

```text
Series DataFrame
              director  avg_vote
title                           
Steel Bridge  Ana Ruiz       8.3
Night Signal  Ben Cole       8.9
```

Single brackets → a Series; a **list** of names → a DataFrame.

## 2. Rows: loc (by label) and iloc (by position)

```python
print(df.loc["Red Canyon", "director"])
print(df.iloc[0]["year"])
print(df.iloc[1:4].index.tolist())
print(df.loc["Night Signal":"Quiet Orbit"].index.tolist())
```

```text
Ana Ruiz
1995
['Night Signal', 'Red Canyon', 'Quiet Orbit']
['Night Signal', 'Red Canyon', 'Quiet Orbit']
```

`iloc[1:4]` stops **before** position 4; `loc["A":"B"]` **includes** "B".

## 3. Conditions

```python
high = df[df["avg_vote"] >= 8.0]
print(len(high))
both = df[(df["director"] == "Ana Ruiz") & (df["avg_vote"] > 7)]
print(both.index.tolist())
either = df[(df["genre"] == "Comedy") | (df["duration"] > 150)]
print(len(either))
print(df[df["director"].isin(["Fay Lin", "Eli Moss"])].shape[0])
```

```text
5
['Steel Bridge', 'Dust Runner', 'Open Loop']
8
7
```

Use `&` (and), `|` (or), and parentheses around each comparison.

## 4. Sorting and apply

```python
top = df.sort_values(by="avg_vote", ascending=False)
print(top.index[:3].tolist())
print(df.sort_values(by=["year", "avg_vote"], ascending=[False, False]).index[0])

def rating_category(x):
    if x >= 8.0:
        return "good"
    return "average"

df["category"] = df["avg_vote"].apply(rating_category)
print(df["category"].value_counts()["good"])
```

```text
['Dust Runner', 'Night Signal', 'Iron Valley']
Open Loop
5
```
