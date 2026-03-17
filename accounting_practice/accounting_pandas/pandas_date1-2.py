import pandas as pd
df = pd.read_csv("transactions1.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

result = (
    df
    .groupby(["month","account"])["debit"]
    .sum()
    .loc[2]
    .sort_values(ascending=False)
    .head(3)
)
print(result)