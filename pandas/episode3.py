from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

folder = Path(__file__).parent
students = pd.read_excel(folder / "students_info.xlsx")
results = pd.read_html(folder / "results_ejudge.html")[0]
data = students.merge(results, left_on="login", right_on="User")

data.groupby("group_faculty")["Solved"].mean().plot.bar(rot=0)
plt.xlabel("Факультетская группа")
plt.ylabel("Среднее количество решённых задач")
plt.tight_layout()
plt.savefig(folder / "faculty.png")
plt.close()

data.groupby("group_out")["Solved"].mean().plot.bar(rot=0)
plt.xlabel("Группа по информатике")
plt.ylabel("Среднее количество решённых задач")
plt.tight_layout()
plt.savefig(folder / "informatics.png")
plt.close()

passed = data[(data["G"] >= 10) | (data["H"] >= 10)]
print(passed.groupby("group_faculty").size())
print(passed.groupby("group_out").size())

print("Строк без логина:", students["login"].isna().sum())
print("Логины без данных о группах:")
print(results.loc[~results["User"].isin(students["login"]), "User"].to_list())
