import pandas as pd

df = pd.read_csv("transactions.csv")
df["balance"] = df["debit"] - df["credit"]

result = (
    df[df["debit"] > 0]
    .sort_values("debit", ascending=False)
    .head(3)
)
print(result)