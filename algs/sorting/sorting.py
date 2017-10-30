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


class QuickSort:

    def __init__(self, items):
        self._items = items
        self._size = len(items)

    def _partition(self, low, high):
        pivot = self._items[low]
        x, y = low + 1, high

        while True:
            while x <= y and self._items[x] <= pivot:
                x += 1
            while y >= x and self._items[y] >= pivot:
                y -= 1

            if y < x:
                break

            self._items[x], self._items[y] = self._items[y], self._items[x]

        self._items[low], self._items[y] = self._items[y], self._items[low]

        return y

    def _sort(self, low, high):
        if low >= high:
            return

        idx = self._partition(low, high)
        self._sort(low, idx - 1)
        self._sort(idx + 1, high)

    def sort(self):
        self._sort(0, self._size - 1)

    def swap(self, x, y):
        self._items[x], self._items[y] = self._items[y], self._items[x]

    def _quick3way(self, low, high):
        if low >= high:
            return

        lt, eq, gt = low, low+1, high
        pivot = self._items[low]

        while eq <= gt:
            if self._items[eq] < pivot:
                self.swap(lt, eq)
                lt += 1
                eq += 1
            elif self._items[eq] > pivot:
                self.swap(eq, gt)
                gt -= 1
            else:
                eq += 1

        self._quick3way(low, lt - 1)
        self._quick3way(gt + 1, high)

    def quick3way(self):
        self._quick3way(0, self._size - 1)

    def is_sorted(self):
        for n in range(1, self._size):
            if self._items[n] < self._items[n-1]:
                return False
        return True


class HeapSort:

    def __init__(self, items):
        self._items = items
        self._size = len(items)

    def is_sorted(self):
        for n in range(1, self._size):
            if self._items[n] < self._items[n-1]:
                return False
        return True

    def _swap(self, x, y):
        self._items[x], self._items[y] = self._items[y], self._items[x]

    def _heapify(self, end, idx):
        l = 2 * idx + 1
        r = 2 * (idx + 1)
        max = idx

        if l < end and self._items[idx] < self._items[l]:
            max = l

        if r < end and self._items[max] < self._items[r]:
            max = r

        if max != idx:
            self._swap(idx, max)
            self._heapify(end, max)

    def sort(self):

        k = self._size // 2 - 1
        while k >= 0:
            self._heapify(self._size, k)
            k -= 1

        k = self._size - 1
        while k > 0:
            self._swap(k, 0)
            self._heapify(k, 0)
            k -= 1


if __name__ == "__main__":
    items = [random.randint(0, 999) for _ in range(16)]
    # sort = Sort(items)
    # sort = MergeSort(items)
    # sort = QuickSort(items)
    sort = HeapSort(items)
    print(sort._items, sort.is_sorted())
    # sort.shell()
    # print(sort._items, sort.is_sorted())
    sort.sort()
    print(sort._items, sort.is_sorted())
