def calculate_charges(min1, min2_10, min11, minutes):
    cost = 0  # start with zero cost

    # First minute
    if minutes >= 1:
        cost = cost + min1  # add cost of first minute

    # Minutes 2 to 10
    if minutes > 1:
        # number of minutes in this block = min(9, minutes-1)
        #Number of minutes = min(9, 11-1) = 9
        #Cost = 3 + 9*1 = 12
        cost = cost + min(9, minutes - 1) * min2_10

    # Minutes after 10
    if minutes > 10:
        # remaining minutes after 10th minute
        cost = cost + (minutes - 10) * min11

    return cost

# Example
print(calculate_charges(3, 1, 2, 9))