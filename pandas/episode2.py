import pandas as pd
import matplotlib.pyplot as plt

flights = pd.read_csv("flights.csv", index_col=0)
result = flights.groupby("CARGO").agg({"CARGO": "count", "PRICE": "sum", "WEIGHT": "sum"})
result.columns = ["Рейсы", "Стоимость", "Масса"]
print(result)

result.plot.bar(subplots=True, legend=False, figsize=(8, 8), rot=0)
plt.tight_layout()
plt.savefig("flights.png")
plt.show()
