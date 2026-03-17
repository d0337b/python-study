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

# 중요 df[조건] → sort_values → head(N) 이런식으로가야하는거임
# for ex)
result = df[df["debit"] > 0] \
            .sort_values("balance", ascending=False) \
           .head(3)

#값만 뽑기 -> top_balance = result["balance"].iloc[0]
#계정 이름만 뽑기 -> top_account = result.index[0]