from pathlib import Path

import matplotlib.pyplot as plt

folder = Path(__file__).parent
output = folder / "results" / "episode1"
output.mkdir(parents=True, exist_ok=True)

for path in sorted((folder / "data" / "episode1").glob("*.dat")):
    x = []
    y = []

    with open(path) as file:
        n = int(file.readline())
        for i in range(n):
            a, b = file.readline().split()
            x.append(float(a))
            y.append(float(b))

    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, s=10)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title(f"{path.stem}: количество точек — {n}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.savefig(output / f"{path.stem}.png")
    plt.close()
