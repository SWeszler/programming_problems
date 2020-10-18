def k_closest_points(points, K):
    points.sort(key = lambda P: P[0]**2 + P[1]**2)
    return points[:K]

def dist(point):
    return point[0]**2 + point[1]**2

def quicksort(points):
    """This function is imitating quick sort algorithm.
    It's a good example of Divide and Conquer approach."""

    if len(points) <= 1:
        return points

    pivot = points.pop()

    points_lower = []
    points_higher = []

    for point in points:
        if dist(point) > dist(pivot):
            points_higher.append(point)
        else:
            points_lower.append(point)

    return quicksort(points_lower) + [pivot] + quicksort(points_higher)

def k_closest_points_naive(points, K):
    """NAIVE approach, not recommended."""
    
    points = quicksort(points)
    return points[:K]