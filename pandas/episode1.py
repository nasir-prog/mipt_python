from pathlib import Path

import pandas as pd

folder = Path(__file__).parent
transactions = pd.read_csv(folder / "transactions.csv", index_col=0)
payments = transactions[transactions["STATUS"] == "OK"]

print(payments.nlargest(3, "SUM"))
print(payments.loc[payments["CONTRACTOR"] == "Umbrella, Inc", "SUM"].sum())
