class UF:

    def __init__(self, count):
        self._count = count
        self._idx = [n for n in range(count)]

    def find(self, p):
        return self._idx[p]

    def count(self):
        return self._count

    def union(self, p, q):
        pidx = self.find(p)
        qidx = self.find(q)

        if pidx == qidx:
            return

        for n in range(len(self._idx)):
            if self._idx[n] == pidx:
                self._idx[n] = qidx

        self._count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class WeightedQuickUnionUF:

    def __init__(self, count):
        self._idx = [n for n in range(count)]
        self._weight = [n for n in range(count)]
        self._count = count

    def find(self, p):
        while p != self._idx[p]:
            p = self._idx[p]
        return p

    def count(self):
        return self._count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        x = self.find(p)
        y = self.find(q)

        if x == y:
            return

        if self._weight[x] < self._weight[y]:
            self._idx[x] = y
            self._weight[y] += self._weight[x]
        else:
            self._idx[y] = x
            self._weight[x] += self._weight[y]
        self._count -= 1


def union(UF, _file):
    with open(_file, 'r') as reader:
        lines = reader.readlines()

    count = int(lines[0])
    uf = UF(count)
    for line in lines[1:]:
        p, q = map(int, line.split())
        if uf.connected(p, q):
            continue
        uf.union(p, q)

    print(uf.count(), " compoments")


if __name__ == "__main__":
    union(UF, "/home/wongxinjie/Downloads/algs4-data/largeUF.txt")
