transactions = [
    {"account":"cash", "debit":1000, "credit":0},
    {"account":"sales", "debit":0, "credit":1000},
    {"account":"cash", "debit":500, "credit":0},
    {"account":"sales", "debit":0, "credit":500},
    {"account":"expense", "debit":200, "credit":0} #차변대변계정
]
result = {}
for t in transactions:
    account = t["account"]
    debit = t["debit"]
    if account in result:
        result[account] += debit
    else:
        result[account] = debit
print(result)
