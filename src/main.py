import algorithms.hassan_strike_algorithm_ver_1 as offline
import algorithms.strike_greedy_online_v1 as greedy
import algorithms.strike_greedy_ratio_online_v1 as greedy_ratio
from instance_parser import load_instance

# Instance files:
I_random = "random.txt"
I_high_first = "high-first-not-enough-later.txt"
I_cheaper_later = "high-first-high-first-cheaper-later.txt"

if __name__ == '__main__':
    random_instance = load_instance(I_random)

    greedy_ratio_results = greedy_ratio.strike_algorithm(*random_instance)
    print(greedy_ratio_results)

    greedy_results = greedy.strike_algorithm(*random_instance)
    print(greedy_results)
    greedy.strike_algorithm_print(*random_instance, debug_info=True, extra_info=True)

    offline.strike_algorithm(*random_instance, debug_info=True, extra_info=False)
