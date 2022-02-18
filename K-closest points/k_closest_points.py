import math


def kClosest(points, k):
    points.sort(key=lambda arg: arg[0] ** 2 + arg[1] ** 2)
    return points[:k]


print(kClosest([[0, 1], [1, 0]], 2))
