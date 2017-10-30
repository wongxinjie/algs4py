class MaxPQ:

    def __init__(self):
        self._size = 0
        self._items = [None]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def insert(self, item):
        self._items.append(item)
        self._size += 1
        self._swim(self._size)

    def swap(self, x, y):
        self._items[x], self._items[y] = self._items[y], self._items[x]

    def less(self, x, y):
        return self._items[x] < self._items[y]

    def delete_max(self):
        key = self._items[1]
        self.swap(1, self._size)
        self._size -= 1
        self._items.pop()
        self._sink(1)
        return key

    def _swim(self, k):
        while k > 1 and self.less(k // 2, k):
            self.swap(k // 2, k)
            k = k // 2

    def _sink(self, k):
        while 2 * k <= self._size:
            x = k * 2

            if x < self._size and self.less(x, x+1):
                x += 1

            if not self.less(k, x):
                break

            self.swap(k, x)
            k = x


class IndexMinPQ:

    def __init__(self, n):
        self._max_size = n
        self._size = 0
        self._items = [None] * (self._max_size + 1)
        self._keys = [None] * (self._max_size + 1)
        self._rkeys = [-1] * (self._max_size + 1)

    def insert(self, k, item):
        """插入一个元素，与索引k相关联
        """
        self._size += 1
        self._keys[k] = self._size
        self._rkeys[self._size] = k
        self._items[k] = item
        self._sink(self._size)

    def change(self, k, item):
        """将索引为k的元素设为item
        """
        self._items[k] = item
        self._swim(self._keys[k])
        self._sink(self._keys[k])

    def contains(self, k):
        """是否存在索引为k的元素
        """
        return self._size > k and self._rkeys[k] is not None

    def delete(self, k):
        """删除索引k及其相关的元素
        """
        self._size -= 1
        idx = self._keys[k]
        self._swap(idx, self._size)
        self._swim(idx)
        self._sink(idx)
        self._items[k] = None
        self._rkeys[k] = 1

    def min(self):
        return self._items[self._keys[1]]

    def min_index(self):
        return self._keys[1]

    def delete_min(self):
        index_of_min = self._keys[1]
        self._size -= 1
        self._swap(1, self._size)
        self._sink(1)
        self._items[self._keys[self._size+1]] = None
        self._rkeys[self._keys[self._size+1]] = -1
        return index_of_min

    def is_empty(self):
        return bool(self._size)

    def size(self):
        return self._size

    def _swim(self, k):
        while k > 1 and self.less(k // 2, k):
            self.swap(k // 2, k)
            k = k // 2

    def _sink(self, k):
        while 2 * k <= self._size:
            x = k * 2

            if x < self._size and self.less(x, x+1):
                x += 1

            if not self.less(k, x):
                break

            self.swap(k, x)
            k = x

    def _swap(self, x, y):
        self._items[x], self._items[y] = self._items[y], self._items[x]


if __name__ == "__main__":
    import random

    # pq = MaxPQ()
    # for _ in range(10):
    #     pq.insert(random.randint(0, 100))

    # print(pq._items)
    # print(pq.delete_max())
    # print(pq._items)
    # print(pq.delete_max())
    # print(pq._items)

    index_pq = IndexMinPQ(10)
    for n in range(1, 11):
        index_pq.insert(n, random.randint(0, 100))
    print(index_pq._items, index_pq._keys, index_pq._rkeys)
