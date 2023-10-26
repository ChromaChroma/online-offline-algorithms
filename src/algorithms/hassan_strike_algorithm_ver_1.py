from queue import PriorityQueue
DayData = (int, int, int)  # tuple (seats, seat price, hotel price)
AlgResult = (int, [(int, int)])  # tuple (total_cost, list of people sent and remaining each day)


def strike_algorithm(n: int, m: int, days: [DayData]) -> AlgResult:
    """
    Offline (optimal) algorithm for Strike

    :param n: Number of people to be sent back
    :param m: Days within all n people should be sent back
    :param days: m long list of DayData, a tuple with (amount_of_seats, flight_cost, hotel_cost)

    :returns: AlgResult - Algorithm result type containing the total cost and the decisions
    """

    # Initialize priority queue for cumulative costs
    ordered_days = PriorityQueue(m)

    # Initialize variables
    cumulative_cost = 0

    # For each day
    for i, (seat, flight_cost, hotel_cost) in enumerate(days):
        # Calculate the cumulative price to send a person back
        price = flight_cost + cumulative_cost

        # Add cost price and day information to the priority queue
        ordered_days.put((price, (i, seat, flight_cost, hotel_cost)))

        # Update the cumulative cost of lodging a person up to the current day
        cumulative_cost = cumulative_cost + hotel_cost

    # Initialize variables (remaining people to n)
    remaining = n
    cost_tracker = 0
    people = []

    # While there are days in the PriorityQueue and people remaining to be sent back
    while not ordered_days.empty() and remaining > 0:
        # Get next cheapest day to send people back
        (price, (day, seat, flight_cost, hotel_cost)) = ordered_days.get()

        # Decide how many people to sent back: min(seats, n)
        travelers = min(seat, remaining)

        # Reduce remaining people
        remaining = remaining - travelers

        # Update total cost
        cost_tracker += (travelers * flight_cost) + (hotel_cost * remaining)

        # Append decision to the decisions
        people.append((travelers, remaining))

    # Return results
    return cost_tracker, people
