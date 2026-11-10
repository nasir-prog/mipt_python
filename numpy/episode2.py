from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

folder = Path(__file__).resolve().parent
results = folder / "results"
results.mkdir(exist_ok=True)

for path in sorted((folder / "signals").glob("*.dat")):
    signal = np.loadtxt(path, ndmin=1)
    filtered = np.array([signal[max(0, i - 9):i + 1].mean() for i in range(len(signal))])

    fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharex=True, sharey=True)
    axes[0].plot(signal)
    axes[0].set_title("Сырой сигнал")
    axes[1].plot(filtered)
    axes[1].set_title("После фильтра")

    for ax in axes:
        ax.set_xlabel("Отсчёт")
        ax.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(results / (path.stem + ".png"))
    plt.close(fig)
