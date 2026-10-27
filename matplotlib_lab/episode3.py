import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


ROOT = Path(__file__).resolve().parent


def read_results(path):
    results = []
    with Path(path).open(encoding="utf-8-sig", newline="") as file:
        for number, row in enumerate(csv.reader(file, delimiter=";"), start=1):
            if not row or all(not field.strip() for field in row):
                continue
            if len(row) != 3:
                raise ValueError(f"Строка {number}: ожидались преподаватель, группа и оценка")
            teacher, group, mark = (field.strip() for field in row)
            results.append((teacher, group, int(mark)))
    if not results:
        raise ValueError("Файл оценок пуст")
    return results


def split_results(results, column):
    grouped = defaultdict(list)
    for row in results:
        grouped[row[column]].append(row[2])
    return dict(sorted(grouped.items()))


def draw_distribution(ax, grouped, marks, title, xlabel):
    labels = list(grouped)
    positions = list(range(len(labels)))
    bottom = [0] * len(labels)
    colors = plt.get_cmap("tab10")
    for index, mark in enumerate(marks):
        counts = [grouped[label].count(mark) for label in labels]
        ax.bar(positions, counts, bottom=bottom, label=str(mark), color=colors(index % 10), width=0.72)
        bottom = [total + count for total, count in zip(bottom, counts)]
    ax.set_xticks(positions, labels)
    ax.set(title=title, xlabel=xlabel, ylabel="Количество студентов")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)
    ax.legend(title="Оценка", bbox_to_anchor=(1.02, 1), loc="upper left")


def describe(grouped):
    return "; ".join(f"{label}: {mean(marks):.2f} (n={len(marks)})" for label, marks in grouped.items())


def extremes(grouped, highest):
    value = (max if highest else min)(mean(marks) for marks in grouped.values())
    labels = [label for label, marks in grouped.items() if mean(marks) == value]
    return ", ".join(labels), value


def main(data_path=None, output_dir=None):
    data_path = Path(data_path) if data_path is not None else ROOT / "data" / "episode3" / "students.csv"
    output_dir = Path(output_dir) if output_dir is not None else ROOT / "results" / "episode3"
    output_dir.mkdir(parents=True, exist_ok=True)
    results = read_results(data_path)
    teachers = split_results(results, 0)
    groups = split_results(results, 1)
    marks = sorted({mark for _, _, mark in results})
    fig, axes = plt.subplots(2, 1, figsize=(11, 9), layout="constrained")
    draw_distribution(axes[0], teachers, marks, "Распределение оценок по преподавателям", "Преподаватель")
    draw_distribution(axes[1], groups, marks, "Распределение оценок по группам", "Группа")
    fig.savefig(output_dir / "marks_distribution.png", dpi=160)
    plt.close(fig)
    easiest, highest = extremes(teachers, True)
    strictest, lowest = extremes(teachers, False)
    weakest, group_lowest = extremes(groups, False)
    summary = "\n".join([
        f"Всего студентов: {len(results)}",
        f"Средние оценки по преподавателям: {describe(teachers)}",
        f"Средние оценки по группам: {describe(groups)}",
        f"Предположительно наиболее лояльные преподаватели: {easiest} (средняя {highest:.2f}).",
        f"Предположительно наиболее строгие преподаватели: {strictest} (средняя {lowest:.2f}).",
        f"Группы с наименьшей средней оценкой: {weakest} (средняя {group_lowest:.2f}).",
        "Это предположения по средним оценкам: состав студентов у преподавателей может различаться.",
        "Низкая средняя оценка группы сама по себе не доказывает небрежность студентов.",
    ]) + "\n"
    (output_dir / "conclusions.txt").write_text(summary, encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(main())
