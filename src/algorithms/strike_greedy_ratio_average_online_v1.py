
def strike_algorithm(n: int, m: int, days: [(int, int, int)]) -> (int, [(int, int)]):
    """
    Greedy online algorithm with ratio

    :param n: Number of people to be sent back
    :param m: Days within all n people should be sent back
    :param days: m long list of tuple with information per day including
                (amount_of_seats, flight_cost, hotel_cost)
    :param ratio: Ratio of flight price to choose flight over hotel stay, 0≤ratio≤1

    :returns: tuple (total_cost, list of people sent and remaining each day)
    """
    total_cost, cumulative_cost = 0,0

    sent_and_remaining = []

    flight_ratio, flight_costs = 0.2, []


    for i, (seats, flight_cost, hotel_cost) in enumerate(days):
        if n == 0:
            # Fill remaining days with (0,0)
            sent_and_remaining += [(0, 0) for _ in range(1, m - i)]
            break

        avg_f = sum(flight_costs) / len(flight_costs) if len(flight_costs) > 1 else 0
        print(avg_f)
        if flight_cost > avg_f * (1.0 - flight_ratio) or flight_cost > avg_f * (1.0 + flight_ratio):
        # if (flight_cost <= hotel_cost) or (flight_cost * ratio <= hotel_cost):
            people_sent_back = seats if seats <= n else n

            price = flight_cost + cumulative_cost
            total_cost += price * people_sent_back
            n -= people_sent_back

            sent_and_remaining.append((people_sent_back, n))
        else:
            sent_and_remaining.append((0, n))

        flight_costs.append(flight_cost)
        cumulative_cost += hotel_cost

    return total_cost, sent_and_remaining
