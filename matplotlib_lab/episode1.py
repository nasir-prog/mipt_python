from pathlib import Path
from math import ceil

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent


def read_points(path):
    with Path(path).open(encoding="utf-8-sig") as file:
        count = int(file.readline())
        if count <= 0:
            raise ValueError(f"{path}: количество точек должно быть положительным")
        points = []
        for _ in range(count):
            coordinates = list(map(float, file.readline().split()))
            if len(coordinates) != 2:
                raise ValueError(f"{path}: ожидалась пара координат")
            points.append(coordinates)
    return points


def draw_details(points, path, output_dir):
    x, y = zip(*points)
    distance = max(max(x) - min(x), max(y) - min(y)) / 20
    remaining = set(range(len(points)))
    groups = []
    while remaining:
        group = [remaining.pop()]
        for index in group:
            px, py = points[index]
            nearby = {
                other for other in remaining
                if (points[other][0] - px) ** 2 + (points[other][1] - py) ** 2 <= distance ** 2
            }
            remaining.difference_update(nearby)
            group.extend(sorted(nearby))
        groups.append(group)
    if not 2 <= len(groups) <= 12 or max(map(len, groups)) < 20:
        return
    groups.sort(key=lambda group: min(points[index][0] for index in group))
    columns = min(3, len(groups))
    rows = ceil(len(groups) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(5 * columns, 4 * rows), squeeze=False, layout="constrained")
    for ax, group in zip(axes.flat, groups):
        gx, gy = zip(*(points[index] for index in group))
        ax.scatter(gx, gy, s=16, alpha=0.65)
        ax.set_aspect("equal", adjustable="box")
        ax.margins(0.15)
        ax.set(xlabel="X", ylabel="Y", title=f"Точек: {len(group)}")
        ax.grid(alpha=0.25)
    for ax in list(axes.flat)[len(groups):]:
        ax.set_visible(False)
    fig.suptitle(f"{path.stem}: увеличенные фрагменты", fontsize=16)
    fig.savefig(output_dir / f"{path.stem}_details.png", dpi=160)
    plt.close(fig)


def main(data_dir=None, output_dir=None):
    data_dir = Path(data_dir) if data_dir is not None else ROOT / "data" / "episode1"
    output_dir = Path(output_dir) if output_dir is not None else ROOT / "results" / "episode1"
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = sorted(path for path in data_dir.iterdir() if path.is_file())
    if not paths:
        raise ValueError(f"Нет файлов с точками: {data_dir}")
    for path in paths:
        points = read_points(path)
        x, y = zip(*points)
        width = max(x) - min(x)
        height = max(y) - min(y)
        ratio = width / height if height else 3
        figsize = (10, 5) if ratio >= 1 else (6, 9)
        fig, ax = plt.subplots(figsize=figsize, layout="constrained")
        ax.scatter(x, y, s=26 if len(points) < 100 else 8, color="tab:blue", alpha=0.85)
        ax.set_aspect("equal", adjustable="box")
        ax.margins(0.08)
        ax.set(xlabel="X", ylabel="Y", title=f"{path.stem}: количество точек — {len(points)}")
        ax.grid(alpha=0.25)
        ax.set_axisbelow(True)
        fig.savefig(output_dir / f"{path.stem}.png", dpi=160)
        plt.close(fig)
        draw_details(points, path, output_dir)
    return len(paths)


if __name__ == "__main__":
    print(f"Построено наборов точек: {main()}")
