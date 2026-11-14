## Why it matters

pandas is where data lives in Python: load a spreadsheet-like file, look at it, clean it. A **Series** is one
labeled column; a **DataFrame** is a table of Series sharing an index.

`movies.csv` is **made-up practice data** on 20 films (two have no language listed).

## 1. Creating

```python
import numpy as np
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["b"], len(s))
trilogy = {"title": ["A", "B", "C"], "rating": [8.8, 8.7, 8.9]}
df = pd.DataFrame(trilogy, index=["2001", "2012", "2023"])
print(df)
arr = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=["x", "y"])
print(arr.shape)
```

```text
20 3
     title  rating
2001     A     8.8
2012     B     8.7
2023     C     8.9
(2, 2)
```

Each key of the dictionary becomes a **column**.

## 2. Reading and exploring

```python
movies = pd.read_csv("movies.csv")
print(movies.shape)
print(movies.head(3))
print(list(movies.columns))
```

```text
(20, 8)
          title  year  director   genre  duration  avg_vote  votes language
0  Steel Bridge  1995  Ana Ruiz  Comedy        87       8.3  34868  Spanish
1  Night Signal  2016  Ben Cole  Comedy       113       8.9  77616  English
2    Red Canyon  2003  Ana Ruiz  Sci-Fi       159       6.1  50818  English
['title', 'year', 'director', 'genre', 'duration', 'avg_vote', 'votes', 'language']
```

```python
movies.info()
```

```text
<class 'pandas.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 8 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   title     20 non-null     str    
 1   year      20 non-null     int64  
 2   director  20 non-null     str    
 3   genre     20 non-null     str    
 4   duration  20 non-null     int64  
 5   avg_vote  20 non-null     float64
 6   votes     20 non-null     int64  
 7   language  18 non-null     str    
dtypes: float64(1), int64(3), str(4)
memory usage: 1.4 KB
```

```python
print(movies["avg_vote"].describe().round(2))
print(movies["genre"].value_counts())
```

```text
count    20.00
mean      6.98
std       1.24
min       5.30
25%       5.88
50%       6.95
75%       8.00
max       9.00
Name: avg_vote, dtype: float64
genre
Sci-Fi    6
Action    6
Comedy    5
Drama     3
Name: count, dtype: int64
```

`read_csv("file.csv", index_col="title")` uses a column as the row labels. `.tail(n)` shows the last rows.

## 3. Renaming, missing values, duplicates

```python
movies = movies.rename(columns={"avg_vote": "rating"})
print(movies.isnull().sum()["language"])
print(len(movies.dropna()), len(movies))
filled = movies["language"].fillna("unknown")
print(filled.value_counts()["unknown"])
doubled = pd.concat([movies, movies])
print(len(doubled), len(doubled.drop_duplicates()))
```

```text
2
18 20
2
40 20
```

`rename`, `dropna`, `fillna`, `concat` and `drop_duplicates` return **new** DataFrames; assign the result to keep it.
