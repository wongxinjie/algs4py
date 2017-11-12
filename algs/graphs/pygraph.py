class Vertex:
    UNTRACED = 0
    TRACING = 1
    TRACED = 2

    def __init__(self, key):
        self._key = key
        self._connected_to = {}
        # 0 - untraced, 1 - tracing, 2 - traced
        self._trace_status = self.UNTRACED
        self._distance = 0
        self._predecessor = None
        self._finish = 0

    def add_neighbor(self, neighbor, weight=0):
        self._connected_to[neighbor] = weight

    def __str__(self):
        return str(self._key) + 'conncted to ' + str([x.key for x in self._connected_to])

    def get_connections(self):
        return self._connected_to.keys()

    def get_id(self):
        return self._key

    def get_weight(self, neighbor):
        return self._connected_to[neighbor]

    def is_untraced(self):
        return self._trace_status == self.UNTRACED

    def set_untraced(self):
        self._trace_status = self.UNTRACED

    def set_traced(self):
        self._trace_status = self.TRACED

    def set_tracing(self):
        self._trace_status = self.TRACING

    def set_distance(self, n):
        self._distance = n

    def get_distance(self):
        return self._distance

    def set_predecessor(self, v):
        self._predecessor = v

    def get_predecessor(self):
        return self._predecessor

    def set_finish(self, n):
        self._finish = n

    def __eq__(self, other):
        return (self._distance == other._distance and self._key == other._key)

    def __gt__(self, other):
        return self._distance > other._distance

    def __lt__(self, other):
        self._distance < other._distance


class Graph:

    def __init__(self):
        self._vertlist = {}
        self._num_vertices = 0

    def add_vertex(self, key):
        self._num_vertices += 1
        vert = Vertex(key)
        self._vertlist[key] = vert
        return vert

    def get_vertex(self, key):
        return self._vertlist.get(key)

    def __contains__(self, key):
        return key in self._vertlist

    def add_edge(self, x, y, cost=0):
        if x not in self._vertlist:
            self.add_vertex(x)
        if y not in self._vertlist:
            self.add_vertex(y)

        self._vertlist[x].add_neighbor(self._vertlist[y], cost)

    def get_vertices(self):
        return self._vertlist.keys()

    def __iter__(self):
        return iter(self._vertlist.values())


class DFSGraph(Graph):

    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0

    def dfs(self):
        for v in self:
            if v.is_untraced():
                self.visit(v)

    def visit(self, vertex):
        vertex.set_tracing()
        self.time += 1
        vertex.set_distance(self.time)
        for v in vertex.get_connections():
            if v.is_untraced():
                v.set_predecessor(vertex)
                self.visit(v)
        vertex.set_traced()
        self.time += 1
        vertex.set_finish(self.time)


def main():
    g = Graph()
    for n in range(6):
        g.add_vertex(n)

    print(g._vertlist)

    connections = [(0, 1, 5), (0, 5, 2), (1, 2, 4), (2, 3, 9)]
    for conn in connections:
        g.add_edge(*conn)

    for v in g:
        for conn in v.get_connections():
            print("(%s, %s)" % (v.get_id(), conn.get_id()))


if __name__ == "__main__":
    main()
