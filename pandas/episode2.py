from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

folder = Path(__file__).parent
flights = pd.read_csv(folder / "flights.csv", index_col=0)
result = flights.groupby("CARGO").agg(
    flights=("CARGO", "size"),
    price=("PRICE", "sum"),
    weight=("WEIGHT", "sum")
)
print(result)

result.plot.bar(
    subplots=True, legend=False, figsize=(9, 10), rot=0,
    title=["Количество рейсов", "Общая стоимость грузов", "Общая масса грузов"]
)
plt.tight_layout()
plt.savefig(folder / "flights.png")
plt.close()
