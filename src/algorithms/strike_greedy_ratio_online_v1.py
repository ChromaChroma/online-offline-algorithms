DayData = (int, int, int)  # tuple (seats, seat price, hotel price)
AlgResult = (int, [(int, int)])  # tuple (total_cost, list of people sent and remaining each day)


def strike_algorithm(n: int, m: int, days: [DayData], ratio: float = 1) -> AlgResult:
    """
    Greedy online algorithm with ratio for Strike

    :param n: Number of people to be sent back
    :param m: Days within all n people should be sent back
    :param days: m long list of DayData, a tuple with (amount_of_seats, flight_cost, hotel_cost)
    :param ratio: Ratio of flight price to choose flight over hotel stay, 0≤ratio≤1

    :returns: AlgResult - Algorithm result type containing the total cost and the decisions
    """
    # Initialize variables
    total_cost, cumulative_cost = 0, 0
    sent_and_remaining = []

    # For each i-th day
    for i, (seats, flight_cost, hotel_cost) in enumerate(days):
        # If all people have been sent back
        if n == 0:
            # Fill remaining days with (0,0)
            sent_and_remaining += [(0, 0) for _ in range(1, m - i)]
            break

        # If flight price or flight price with ratio is cheaper than the hotel cost, sent people back
        if (flight_cost <= hotel_cost) or (flight_cost * ratio <= hotel_cost):
            #  Decide how many people to sent back: min(seats, n)
            people_sent_back = seats if seats <= n else n

            # Calculate prices, costs and adjust n
            price = flight_cost + cumulative_cost
            total_cost += price * people_sent_back
            n -= people_sent_back

            # Append decision to the decisions
            sent_and_remaining.append((people_sent_back, n))
        else:
            # Append decision to the decisions
            sent_and_remaining.append((0, n))

        # Update the cumulative cost of lodging a person up to the current day
        cumulative_cost += hotel_cost

    # Return results
    return total_cost, sent_and_remaining
