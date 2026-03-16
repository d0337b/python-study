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
        result[account] = result.get(account, 0) + balance
print(result) 