import algorithms.hassan_strike_algorithm_ver_1 as offline
import algorithms.strike_greedy_online_v1 as greedy
import algorithms.strike_greedy_ratio_online_v1 as greedy_ratio
from instance_parser import load_instance
from plotting import *
from time import perf_counter_ns


DayData = (int, int, int)
AlgResult = (int, [(int, int)])


def measure_computation_time(algorithm, instance, **args) -> (float, float, float, AlgResult):
    time = []
    res = None

    # Repeat performance test 100 times
    for i in range(0, 10_000):
        # start time
        start = perf_counter_ns()

        # Function to measure
        res = algorithm(*instance, **args)

        # end time
        stop = perf_counter_ns()
        time.append(stop - start)

    max_value = max(time)
    min_value = min(time)
    avg = sum(time) / len(time)
    return time, avg, min_value, max_value, res


def print_res(alg_name, avg, min_v, max_v):
    print(f"{alg_name} in avg: {avg} ns. With max time: {max_v} ns and min time: {min_v} ns")


def run_test(filename: str):
    instance = load_instance(filename)

    (o_times, o_avg, o_min, o_max, (o_c, o_p)) = measure_computation_time(offline.strike_algorithm, instance)
    (g_times, g_avg, g_min, g_max, (g_c, g_p)) = measure_computation_time(greedy.strike_algorithm, instance)
    (gr_times, gr_avg, gr_min, gr_max, (gr_c, gr_p)) \
        = measure_computation_time(greedy_ratio.strike_algorithm, instance, ratio=0.8)

    print_res("Offline", o_avg, o_min, o_max)
    print(f"{o_c} using: {o_p}")
    print_res("Greedy", g_avg, g_min, g_max)
    print(f"{g_c} using: {g_p}")
    print_res("Greedy Ratio", gr_avg, gr_min, gr_max)
    print(f"{gr_c} using: {gr_p}")

    boxplot(o_times, title="Offline Algorithm performance")

    all_results = {
        "Offline": o_times,
        "Greedy": g_times,
        "Greedy Ratio": gr_times
    }
    boxplot_all(all_results, title="All Algorithms performance")

    online_results = {
        "Greedy": g_times,
        "Greedy Ratio": gr_times
    }
    boxplot_all(online_results, title="Online Algorithms performance")
