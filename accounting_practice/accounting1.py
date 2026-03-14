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
    ammount = t["debit"] + t["credit"] #차변과 대변을 더해서 계정별로 합산하기
    if account in result:
        result[account] += ammount
    else:
        result[account] = ammount
print(result)
