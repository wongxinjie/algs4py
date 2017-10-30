class Node:

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class SequentialSearchST:

    def __init__(self):
        self.first = None

    def put(self, key, value):
        x = self.first
        while x is not None:
            if x.key == key:
                x.value = value
                return
            x = x.next

        self.first = Node(key, value, self.first)

    def get(self, key):
        x = self.first
        while x is not None:
            if x.key == key:
                return x.value
            x = x.next


class BinarySearchST:

    def __init__(self):
        self._size = 0
        self.keys = []
        self.values = []

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get(self, key):
        if self.is_empty():
            return

        idx = self.rank(key)
        if idx < self._size and self.keys[idx] == key:
            return self.values[idx]

    def put(self, key, value):
        idx = self.rank(key)

        if idx < self._size and self.keys[idx] == key:
            self.values[idx] = value

        self.keys.append(None)
        self.values.append(None)
        for n in range(self._size, idx, -1):
            self.keys[n] = self.keys[n-1]
            self.values[n] = self.keys[n-1]

        self.keys[idx] = key
        self.values[idx] = value
        self._size += 1

    def rank(self, key):
        lo, hi = 0, self._size - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.keys[mid] < key:
                lo = mid + 1
            elif self.keys[mid] > key:
                hi = mid - 1
            else:
                return mid

        return lo
