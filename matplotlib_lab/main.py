import matplotlib

matplotlib.use("Agg")

from episode1 import main as episode1
from episode2 import main as episode2
from episode3 import main as episode3


def main():
    print(f"Эпизод 1: построено наборов точек — {episode1()}")
    print(f"Эпизод 2: построено кадров — {episode2()}")
    print(episode3())


if __name__ == "__main__":
    main()
