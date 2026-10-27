from pathlib import Path

import matplotlib.pyplot as plt

folder = Path(__file__).parent
output = folder / "results" / "episode2"
output.mkdir(parents=True, exist_ok=True)

with open(folder / "data" / "episode2" / "frames.dat") as file:
    lines = file.readlines()

frames = []
all_x = []
all_y = []

for i in range(0, len(lines), 2):
    x = list(map(float, lines[i].split()))
    y = list(map(float, lines[i + 1].split()))
    frames.append((x, y))
    all_x.extend(x)
    all_y.extend(y)

for i in range(len(frames)):
    x, y = frames[i]
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title(f"Кадр {i}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xticks(range(0, 17, 2))
    plt.yticks(range(-8, 13, 2))
    plt.xlim(min(all_x), max(all_x))
    plt.ylim(min(all_y) - 1, max(all_y) + 1)
    plt.grid()
    plt.savefig(output / f"frame_{i:03d}.png")
    plt.close()
