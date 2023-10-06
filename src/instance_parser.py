def load_instance(instance_file) -> (int, int, (int, int, int)):
    """"
    :param str instance_file: File name of the instance
    :returns: A tuple with number of people,
        number of days,
        and a list of tuples with information per day: (amount_of_seats, flight_cost, hotel_cost)
    """
    with open(f"../instances/{instance_file}") as f:
        n = int(f.readline())
        m = int(f.readline())
        days = list()
        for line in f.readlines():
            values = line.split(sep=',')
            seats = int(values[0].strip())
            flight_price = int(values[1].strip())
            hotel_price = int(values[2].strip())
            days.append((seats, flight_price, hotel_price))
        return n, m, days
