import pandas as pd

df = pd.read_csv("transactions.csv")
df["balance"] = df["debit"] - df["credit"]
# 1. 특정 계정만 보기
print(df[df["account"] == "Cash"])

# 2. debit(지출)만 보기
print(df[df["debit"] > 0])

# 3. balance 큰 것만 보기
print(df[df["balance"] > 1000])

# balance 기준 내림차순
print(df.sort_values("balance", ascending=False))
    #여기에 ascending=False).head(5) 하면 상위 5개

#debit 기준 오름차순
print(df.sort_values("debit"))
