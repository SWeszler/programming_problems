def two_city_scheduling(costs):
    A, B = 0, 0
    a, b = 0, 0
    costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
    mid = len(costs)//2
    for c in costs:
        if c[0] < c[1]:
            if a < mid:
                A += c[0]
                a += 1
            else:
                B += c[1]
                b += 1
        else:
            if b < mid:
                B += c[1]
                b += 1
            else:
                A += c[0]
                a += 1
    
    return A + B