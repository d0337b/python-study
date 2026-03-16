# Accounting Practice
# balance = debit - credit
import csv
result = {}
with open("transactions.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        account = row["account"]
        debit = int(row["debit"])
        credit = int(row["credit"])
        balance = debit - credit

        if account not in result:
            result[account] = {
                "debit": 0,
                "credit": 0,
                "balance": 0
            }
        result[account]["debit"] += debit
        result[account]["credit"] += credit
        result[account]["balance"] += balance
print(result) 