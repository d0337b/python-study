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
print(f"{'Account':<12}{'Debit':<10}{'credit':<10}{'Balance':<10}")
for account, data in result.items():
    print(f"{account:<12}{data['debit']:<10}{data['credit']:<10}{data['balance']:<10}")