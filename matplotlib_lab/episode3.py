from pathlib import Path

import matplotlib.pyplot as plt

folder = Path(__file__).parent
output = folder / "results" / "episode3"
output.mkdir(parents=True, exist_ok=True)

students = []
with open(folder / "data" / "episode3" / "students.csv") as file:
    for line in file:
        teacher, group, mark = line.strip().split(";")
        students.append([teacher, group, int(mark)])

names = [
    ["prep1", "prep2", "prep3", "prep4", "prep5", "prep6", "prep7"],
    ["751", "752", "753", "754", "755", "756"]
]
titles = ["Оценки по преподавателям", "Оценки по группам"]

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

for number in range(2):
    bottom = [0] * len(names[number])

    for mark in range(3, 11):
        counts = []
        for name in names[number]:
            count = 0
            for student in students:
                if student[number] == name and student[2] == mark:
                    count += 1
            counts.append(count)

        axes[number].bar(names[number], counts, bottom=bottom, label=str(mark))
        for i in range(len(bottom)):
            bottom[i] += counts[i]

    axes[number].set_title(titles[number])
    axes[number].set_ylabel("Количество студентов")
    axes[number].legend(title="Оценка", loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig(output / "marks_distribution.png")
plt.close()
