from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

folder = Path(__file__).resolve().parent
results = folder / "results"
results.mkdir(exist_ok=True)

u = np.loadtxt(folder / "start.dat.txt")
states = [u]

for _ in range(255):
    u = (u + np.roll(u, 1)) / 2
    states.append(u)

fig, axes = plt.subplots(1, 2, figsize=(9, 4), layout="constrained")
image = axes[0].imshow(states, origin="lower", aspect="auto", interpolation="nearest")
axes[0].set_title("Все шаги")
axes[0].set_xlabel("x")
axes[0].set_ylabel("Шаг")
fig.colorbar(image, ax=axes[0], label="u(x)")

axes[1].plot(states[-1])
axes[1].set_title("Шаг 255")
axes[1].set_xlabel("x")
axes[1].set_ylabel("u(x)")
axes[1].grid(alpha=0.3)

fig.savefig(results / "process.png")
plt.close(fig)
