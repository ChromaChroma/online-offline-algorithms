def strike_algorithm_print(n: int, m: int, days: (int, float, float), extra_info=False, debug_info=False):
    """"
    :param n: Number of people to be sent back
    :param m: Days within all n people should be sent back
    :param days: m long list of tuple with information per day including
                (amount_of_seats, flight_cost, hotel_cost)
    """
    if debug_info:
        print('------------- Online Greedy Algorithm -------------')
        print('------------- Start{Generating Day Values} -------------')

    total_cost = 0
    cumulative_cost = 0
    day_number = 0
    sent_and_remaining = []

    for (seats, flight_cost, hotel_cost) in days:
        if n == 0:
            if debug_info:
                print(f' **: Stopping further calculation, because all people have been sent back')
            break

        people_sent_back = seats if seats <= n else n

        price = flight_cost + cumulative_cost
        total_cost += price * people_sent_back
        n -= people_sent_back

        sent_and_remaining.append((people_sent_back, n))

        if debug_info:
            print(f'day: {day_number}, price:{price}')

        cumulative_cost += hotel_cost
        day_number += 1

    if debug_info:
        print('------------- End{Generating Day Values  } -------------\n')
        if n != 0:
            print(f' **: Not all people have been sent back, {n} remain')
        print(f' **: Total costs: {total_cost}')

    sent_and_remaining += [(0, 0) for _ in range(1, m - day_number)]
    print('sent,remaining  for each day')
    for (travelers, remaining) in sent_and_remaining:
        print(f'{travelers}, {remaining}')


def strike_algorithm(n: int, m: int, days: (int, int, int)):
    """"
    Pure return version of the strike_algorithm_print

    :param n: Number of people to be sent back
    :param m: Days within all n people should be sent back
    :param days: m long list of tuple with information per day including
                (amount_of_seats, flight_cost, hotel_cost)
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
        people_sent_back = seats if seats <= n else n

        price = flight_cost + cumulative_cost
        total_cost += price * people_sent_back
        n -= people_sent_back

        sent_and_remaining.append((people_sent_back, n))

        cumulative_cost += hotel_cost
        day_number += 1

    return total_cost, sent_and_remaining
