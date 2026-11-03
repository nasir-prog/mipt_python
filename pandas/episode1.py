import pandas as pd

transactions = pd.read_csv("transactions.csv", index_col=0)
payments = transactions[transactions["STATUS"] == "OK"]

print(payments.sort_values("SUM", ascending=False).head(3))
print(payments[payments["CONTRACTOR"] == "Umbrella, Inc"]["SUM"].sum())
