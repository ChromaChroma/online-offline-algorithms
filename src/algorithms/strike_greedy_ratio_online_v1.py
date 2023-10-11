"""
Improvements to be added:

* If hotel price > flight, send maximum amount
* If hotel price is, within ratio, slightly lower than flight, send maximum/partial

* Later, alter ratio based on historical data and averages, and compare those with current prices. (with ratio)

"""


def strike_algorithm(n: int, m: int, days: (int, int, int), ratio: float = 1) -> (int, [(int, int)]):
    """
    Greedy online algorithm with ratio

    :param n: Number of people to be sent back
    :param m: Days within all n people should be sent back
    :param days: m long list of tuple with information per day including
                (amount_of_seats, flight_cost, hotel_cost)
    :param ratio: Ratio of flight price to choose flight over hotel stay, 0≤ratio≤1

    :returns: tuple (total_cost, list of people sent and remaining each day)
    """
    total_cost = 0
    cumulative_cost = 0
    day_number = 0

    sent_and_remaining = []

    for (seats, flight_cost, hotel_cost) in days:
        if n == 0:
            # Fill remaining days with (0,0)
            sent_and_remaining += [(0, 0) for _ in range(1, m - day_number)]
            break

        if (flight_cost <= hotel_cost) or (flight_cost * ratio <= hotel_cost):
            people_sent_back = seats if seats <= n else n

            price = flight_cost + cumulative_cost
            total_cost += price * people_sent_back
            n -= people_sent_back

            sent_and_remaining.append((people_sent_back, n))
        else:
            sent_and_remaining.append((0, n))

        cumulative_cost += hotel_cost
        day_number += 1

    return total_cost, sent_and_remaining
