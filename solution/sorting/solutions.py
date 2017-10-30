import heapq
import random


def top_n(array, n):
    return heapq.nlargest(n, array)


def min_n(array, n):
    return heapq.nsmallest(n, array)


if __name__ == "__main__":
    array = [random.randint(0, 1000) for _ in range(1000)]
    print(sorted(array))
    print(top_n(array, 4))
    print(min_n(array, 4))
