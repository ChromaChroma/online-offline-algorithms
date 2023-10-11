import algorithms.hassan_strike_algorithm_ver_1 as offline
import algorithms.strike_greedy_online_v1 as greedy
import algorithms.strike_greedy_ratio_online_v1 as greedy_ratio
import algorithms.strike_greedy_ratio_average_online_v1 as greedy_average
from instance_parser import load_instance
import matplotlib.pyplot as plt
import numpy as np

# Instance files:
I_random = "random.txt"
I_high_first = "high-first-not-enough-later.txt"
I_cheaper_later = "high-first-high-first-cheaper-later.txt"
I_const_hotel = "constant-hotel-price.txt"

if __name__ == '__main__':
    instance = load_instance(I_const_hotel)
    (opt_total, p) = (999999, [])
    opt = 0
    points = []

    (t_offline, p_offline) = offline.strike_algorithm(*instance, debug_info=True, extra_info=True)
    offline_optimal = 3040
    plt.axhline(y=t_offline, color='r', linestyle='-', label='Offline')

    # Greedy algorithm
    (total, people) = greedy.strike_algorithm(*instance)
    print(f"Greedy with total={total},\n for=  {people}")
    plt.axhline(y=total, color='g', linestyle='-', label='Online')
    # greedy.strike_algorithm_print(*random_instance, debug_info=True, extra_info=True)

    for ratio in [i * 0.01 for i in range(1, 100)]:
        (total, people) = greedy_ratio.strike_algorithm(*instance, ratio=ratio)

        if total < opt_total and people[-1][1] == 0:
            points.append(total)
            opt_total = total
            p = people
            opt = ratio

    # Print and plot greedy ratio
    print(f"opt ratio={opt}, with total={opt_total},\n for=  {p}")
    plt.plot(np.array(points), color='b', linestyle='dotted')
    plt.axhline(y=opt_total, color='b', linestyle='-', label='Online Ratio')
    # greedy_ratio_results = greedy_ratio.strike_algorithm(*instance, ratio=1)
    # print(greedy_ratio_results)

    (total, people) = greedy_average.strike_algorithm(*instance)
    print(total)
    print(people)

    plt.legend()
    plt.title("Total price per algorithm (lower = better)")
    plt.ylabel("Total cost")
    plt.show()
