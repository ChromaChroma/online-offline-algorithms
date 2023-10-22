import matplotlib.pyplot as plt
import numpy as np


def boxplot(measurements, title=""):
    data = np.array(measurements)

    # remove largest 1 percentile
    percentile = np.percentile(data, 99)
    data = data[data <= percentile]

    fig = plt.figure(figsize=(10, 4))
    ax = fig.add_subplot()
    ax.set_ylabel("Computation time in ns (Smaller = better)")
    ax.set_title(title)

    ax.boxplot(data)

    # plt.show()
    plt.savefig(f"{title}.png")


def boxplot_all(data: dict, title=""):
    for key, value in data.items():
        # remove largest 1 percentile
        value = np.array(value)
        percentile = np.percentile(value, 99)
        value = value[value <= percentile]
        data[key] = value

    fig = plt.figure(figsize=(10, 4))
    ax = fig.add_subplot()
    ax.set_ylabel("Computation time in ns (Smaller = better)")
    ax.set_title(title)

    ax.boxplot(data.values())
    ax.set_xticklabels(data.keys())

    # plt.show()
    plt.savefig(f"{title}.png")