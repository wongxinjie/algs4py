class MinHeap:

    def __init__(self):
        self._list = [None]
        self._size = 0

    def insert(self, key):
        self._list.append(key)
        self._size += 1
        self._up(self._size)

    def min(self):
        return self._list[1]

    def remove_min(self):
        rv = self._list[1]
        self._list[1] = self._list[self._size]
        self._size -= 1
        self._list.pop()
        self._down(1)
        return rv

    def _swap(self, x, y):
        self._list[x], self._list[y] = self._list[y], self._list[x]

    def _up(self, idx):
        while idx // 2 > 0:
            if self._list[idx] < self._list[idx // 2]:
                self._swap(idx, idx // 2)

            idx = idx // 2

    def _down(self, idx):
        while idx * 2 <= self._size:
            mc = self.min_child_index(idx)
            if self._list[idx] > self._list[mc]:
                self._swap(idx, mc)
            idx = mc

    def min_child_index(self, idx):
        if idx * 2 + 1 > self._size:
            return idx * 2
        else:
            if self._list[idx * 2] < self._list[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1

    def build_head(self, items):
        idx = len(items) // 2
        self._size = len(items)
        self._list = [None] + items[:]
        while idx > 0:
            self._down(idx)
            idx -= 1
