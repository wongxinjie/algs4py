def search(key, array):
    """Binary search, return target index or None
    >>> search(5, [1, 3, 5, 7, 9])
    2
    >>> search(4, [1, 3, 5, 7, 9])
    >>> search(4, [])
    """
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
