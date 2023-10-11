from queue import PriorityQueue


def strike_algorithm(n, m, days, extra_info=False, debug_info=False):
    ordered_days = PriorityQueue(m)

    cumulative_cost = 0
    count = 0

    if debug_info:
        print('------------- Offline Optimal Algorithm -------------')
        print('------------- Start{Generating Day Values} -------------')
    for (seat, flight_cost, hotel_cost) in days:
        price = flight_cost + cumulative_cost

        if debug_info:
            print(f'day: {count}, price:{price}')

        ordered_days.put((price, (count, seat, flight_cost, hotel_cost)))

        cumulative_cost = cumulative_cost + hotel_cost
        count = count + 1
    if debug_info:
        print('------------- End{Generating Day Values  } -------------\n')

    travel_log = list(range(0, m))
    remaining = n
    while not ordered_days.empty():
        (price, (day, seat, flight_cost, hotel_cost)) = ordered_days.get();
        travelers = min(seat, remaining)
        travel_log[day] = travelers
        remaining = remaining - travelers

    remaining = n
    cost_tracker = 0
    people = []
    for i in range(0, m):
        travelers = travel_log[i]
        (seat, flight_cost, hotel_cost) = days[i]
        remaining = remaining - travelers
        cost_tracker += (travelers * flight_cost) + (hotel_cost * remaining)
        people.append((travelers, remaining))
        if (extra_info):
            print(f'travelers: {travelers}, loungers: {remaining};\n'
                  f'travel cost: {travelers * flight_cost}, hotel cost: {hotel_cost * remaining};\n'
                  f'cumulative cost this far: {cost_tracker}\n')
        else:
            print(f'{travelers}, {remaining}')

    return cost_tracker, people
