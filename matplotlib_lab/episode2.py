from math import ceil
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MaxNLocator


ROOT = Path(__file__).resolve().parent


def read_frames(path):
    with Path(path).open(encoding="utf-8-sig") as file:
        rows = [list(map(float, line.split())) for line in file if line.strip()]
    if not rows or len(rows) % 2:
        raise ValueError("Файл должен содержать пары строк X и Y")
    frames = list(zip(rows[::2], rows[1::2]))
    if any(not x or len(x) != len(y) for x, y in frames):
        raise ValueError("В каждом кадре количество координат X и Y должно совпадать")
    return frames


def limits(values):
    lower, upper = min(values), max(values)
    margin = (upper - lower) * 0.05 if upper != lower else 1
    return lower - margin, upper + margin


def draw_frame(ax, frame, number, xlim, ylim):
    x, y = frame
    ax.plot(x, y, color="tab:blue", linewidth=1.6)
    ax.set(xlim=xlim, ylim=ylim, xlabel="X", ylabel="Y", title=f"Кадр {number}")
    ax.xaxis.set_major_locator(MaxNLocator(nbins=8))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=8))
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.grid(which="major", alpha=0.5, linewidth=0.7)
    ax.grid(which="minor", alpha=0.2, linewidth=0.5)
    ax.set_axisbelow(True)


def main(data_path=None, output_dir=None):
    data_path = Path(data_path) if data_path is not None else ROOT / "data" / "episode2" / "frames.dat"
    output_dir = Path(output_dir) if output_dir is not None else ROOT / "results" / "episode2"
    output_dir.mkdir(parents=True, exist_ok=True)
    frames = read_frames(data_path)
    xlim = limits([value for x, _ in frames for value in x])
    ylim = limits([value for _, y in frames for value in y])
    for number, frame in enumerate(frames):
        fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
        draw_frame(ax, frame, number, xlim, ylim)
        fig.savefig(output_dir / f"frame_{number:03d}.png", dpi=160)
        plt.close(fig)
    columns = min(2, len(frames))
    rows = ceil(len(frames) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(6 * columns, 4 * rows), squeeze=False, layout="constrained")
    for number, frame in enumerate(frames):
        draw_frame(axes.flat[number], frame, number, xlim, ylim)
    for ax in list(axes.flat)[len(frames):]:
        ax.set_visible(False)
    fig.suptitle("Эволюция процесса", fontsize=16)
    fig.savefig(output_dir / "all_frames.png", dpi=160)
    plt.close(fig)
    return len(frames)


if __name__ == "__main__":
    print(f"Построено кадров: {main()}")
