import pandas as pd
df = pd.read_csv("transactions.csv")
df["balance"] = df["debit"] - df["credit"]

result =(
    df[df["debit"] > 0]
    .groupby("account")["debit"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
print(result)