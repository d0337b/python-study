import pandas as pd
df = pd.read_csv("transactions.csv")
df["balance"] = df["debit"] - df["credit"]

result = (
    df.groupby("account")[["debit", "credit", "balance"]].sum()
    .sort_values("balance", ascending=False).head(1)
)
print(result)