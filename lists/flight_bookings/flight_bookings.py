
def flight_bookings(bookings, n):
    flights = [0] * n
    
    for booking in bookings:
        flights[booking[0] - 1] += booking[2]
        if booking[1] < n:
            flights[booking[1]] -= booking[2]
            
    s = 0
    for i in range(len(flights)):
        flights[i] += s
        s = flights[i]
            
    return flights



def flight_bookings_slow(bookings, n):
    flights = [0] * n

    for booking in bookings:
        for i in range(booking[0], booking[1] + 1):
            flights[i - 1] += booking[2]

    return flights