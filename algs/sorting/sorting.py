import random


class Sort:

    def __init__(self, items):
        self._items = items
        self._size = len(items)

    def is_sorted(self):
        for n in range(1, self._size):
            if self._items[n] < self._items[n-1]:
                return False
        return True

    def selection(self):
        for x in range(self._size):
            min_idx = x
            for y in range(x+1, self._size):
                if self._items[y] < self._items[min_idx]:
                    min_idx = y

            self._items[x], self._items[min_idx] = self._items[min_idx], self._items[x]

    def insertion(self):
        for x in range(1, self._size):
            for y in range(x, 0, -1):
                if self._items[y] < self._items[y-1]:
                    self._items[y], self._items[y-1] = self._items[y-1], self._items[y]
                else:
                    break

    def shell(self):
        """
        shell sort, magic
        """
        step = 1
        while step < self._size // 3:
            # Why?
            step = 3 * step + 1

        while step >= 1:
            for x in range(step, self._size):
                for y in range(x, step-1, -1):
                    if self._items[y] < self._items[y-step]:
                        self._items[y], self._items[y-step] = self._items[y-step], self._items[y]
                    else:
                        break
            step = step // 3


class MergeSort:

    def __init__(self, items):
        self._items = items
        self._size = len(items)
        self._aux = [0] * self._size

    def _merge(self, low, mid, high):
        x, y = low, mid+1

        for n in range(low, high+1):
            self._aux[n] = self._items[n]

        for n in range(low, high+1):
            if x > mid:
                self._items[n] = self._aux[y]
                y += 1
            elif y > high:
                self._items[n] = self._aux[x]
                x += 1
            elif self._aux[x] > self._aux[y]:
                self._items[n] = self._aux[y]
                y += 1
            else:
                self._items[n] = self._aux[x]
                x += 1

    def _top_down_sort(self, low, high):
        if low >= high:
            return

        mid = low + (high - low) // 2
        self._top_down_sort(low, mid)
        self._top_down_sort(mid+1, high)
        self._merge(low, mid, high)

    def topdown(self):
        self._top_down_sort(0, self._size - 1)

    def bottomup(self):

        sz = 1
        while sz < self._size:
            lo = 0
            while lo < self._size - sz:
                self._merge(lo, lo + sz - 1, min(lo+sz*2 - 1, self._size - 1))
                lo += sz + sz
            sz = sz + sz

    def is_sorted(self):
        for n in range(1, self._size):
            if self._items[n] < self._items[n-1]:
                return False
        return True


if __name__ == "__main__":
    items = [random.randint(0, 999) for _ in range(16)]
    # sort = Sort(items)
    sort = MergeSort(items)
    print(sort._items, sort.is_sorted())
    # sort.shell()
    # print(sort._items, sort.is_sorted())
    sort.bottomup()
    print(sort._items, sort.is_sorted())
