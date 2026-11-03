import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("students_info.xlsx")
results = pd.read_csv("results.csv")
data = students.merge(results, left_on="login", right_on="User")

data.groupby("group_faculty")["Solved"].mean().plot.bar(title="Факультетские группы", rot=0)
plt.ylabel("Среднее число решённых задач")
plt.tight_layout()
plt.savefig("faculty.png")
plt.show()

data.groupby("group_out")["Solved"].mean().plot.bar(title="Группы по информатике", rot=0)
plt.ylabel("Среднее число решённых задач")
plt.tight_layout()
plt.savefig("informatics.png")
plt.show()

passed = data[(data["G"] >= 10) | (data["H"] >= 10)]
print(passed.groupby("group_faculty").size())
print(passed.groupby("group_out").size())

