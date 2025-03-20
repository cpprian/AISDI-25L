from typing import List
import matplotlib.pyplot as plt
import time


def read_words(filename: str, limit: int) -> List[str]:
    output = [None] * limit
    idx = 0
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                if idx < limit:
                    output[idx] = word
                    idx += 1
                else:
                    return output
    return output[:idx]


def load_data(filename: str, times: int, space: List[int]) -> List[List[str]]:
    output = [None] * times
    for i in range(times):
        output[i] = read_words(filename, space[i])
    return output


def make_figure_comparing_time(
    space: List[int],
    time1: List[int],
    time2: List[int],
    title: str,
    label1: str,
    label2: str,
):
    plt.plot(space, time1, label=label1)
    plt.plot(space, time2, label=label2)
    plt.xlabel("Number of elements")
    plt.ylabel("Time in milliseconds")
    plt.title(title)
    plt.legend()
    plt.savefig("img/" + title + ".png")
    plt.close()


def make_figure_comparing_all(
    space: List[int], title: str, labels: List[str], *times: List[int]
):
    idx = 0
    for time in times:
        plt.plot(space, time, label=labels[idx])
        idx += 1
    plt.xlabel("Number of elements")
    plt.ylabel("Time in milliseconds")
    plt.title(title)
    plt.legend()
    plt.savefig("img/" + title + ".png")
    plt.close()


def count_time(fun: callable, data: List[str]) -> int:
    start = time.time()
    fun(data)
    end = time.time()
    print(fun.__name__, end - start)
    return int((end - start) * 1000)
