from collections import deque


class Graph:

    def __init__(self, v=0):
        self._v = v
        self._e = 0
        self._adj = [[] for _ in range(v)]

    def load(self, filename):
        with open(filename, 'r') as reader:
            lines = reader.readlines()

        self._v = int(lines[0])
        self._adj = [[] for _ in range(self._v)]
        self.e = int(lines[1].strip())

        for each in lines[2:]:
            v, w = map(int, each.split())
            self.add_edge(v, w)

    def vertex(self):
        return self._v

    def edge(self):
        return self._e

    def add_edge(self, v, w):
        self._adj[v].append(w)
        self._adj[w].append(v)

    def adj(self, v):
        return self._adj[v]

    def __repr__(self):
        texts = []
        for idx, edges in enumerate(self._adj):
            texts.append('{}: {}'.format(idx, ' '.join(map(str, edges))))

        return '\n'.join(texts)


class DFS:

    def __init__(self, graph, v):
        self._graph = graph
        self._v = v
        self._marked = [False for _ in range(self._graph.vertex())]
        self._count = 0
        self.dfs(v)

    def dfs(self, v):
        self._marked[v] = True
        self._count += 1

        for x in self._graph.adj(v):
            if not self._marked[x]:
                self.dfs(x)

    def connected(self, x):
        return self._marked[x]

    def count(self):
        return self._count


class DFP:
    """Depth First Path"""

    def __init__(self, graph, v):
        self._graph = graph
        self._v = v
        self._marked = [False for _ in range(self._graph.vertex())]
        self._edge_to = [None for _ in range(self._graph.vertex())]
        self._dfs(v)

    def _dfs(self, v):
        self._marked[v] = True

        for x in self._graph.adj(v):
            if not self._marked[x]:
                self._edge_to[x] = v
                self._dfs(x)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = [v]
        x = v
        while x != self._v:
            x = self._edge_to[x]
            path.append(x)

        path.append(self._v)
        return reversed(path)


class BFP:
    """Breath First Path"""

    def __init__(self, graph, v):
        self._graph = graph
        self._v = v
        self._marked = [False] * self._graph.vertex()
        self._edge_to = [None] * self._graph.vertex()
        self._bfs(v)

    def _bfs(self, s):
        queue = deque()
        self._marked[s] = True
        queue.append(s)

        while queue:
            v = queue.popleft()
            for each in self._graph.adj(v):
                if not self._marked[each]:
                    self._edge_to[each] = v
                    self._marked[each] = True
                    queue.append(each)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = [v]
        x = v
        while x != self._v:
            x = self._edge_to[x]
            path.append(x)

        path.append(self._v)
        return reversed(path)


class CC:
    """connected components"""

    def __init__(self, graph):
        self._graph = graph
        self._marked = [False] * self._graph.vertex()
        self._id = [None] * self._graph.vertex()
        self._count = 0

        for n in range(self._graph.vertex()):
            if not self._marked[n]:
                self._dfs(n)
                self._count += 1

    def _dfs(self, v):
        self._marked[v] = True
        self._id[v] = self._count
        for s in self._graph.adj(v):
            if not self._marked[s]:
                self._dfs(s)

    def connected(self, v, w):
        return self._id[v] == self._id[w]

    def cid(self, v):
        return self._id[v]

    def count(self):
        return self._count


class Cycle:

    def __init__(self, graph):
        self._graph = graph
        self._has_cycle = False
        self._marked = [False] * self._graph.vertex()

        for n in range(self._graph.vertex()):
            if not self._marked[n]:
                self._dfs(n, n)

    def _dfs(self, v, u):
        self._marked[v] = True
        for w in self._graph.adj(v):
            if not self._marked[w]:
                self._dfs(w, v)
            else:
                if w != u:
                    self._has_cycle = True

    def has_cycle(self):
        return self._has_cycle


class TwoColor:

    def __init__(self, graph):
        self._graph = graph
        self._marked = [False] * self._graph.vertex()
        self._color = [False] * self._graph.vertex()
        self._is_two_colorable = False

        for v in range(self._graph.vertex()):
            if not self._marked[v]:
                self._dfs(v)

    def _dfs(self, v):
        self._marked[v] = True
        for u in self._graph.adj(v):
            if not self._marked[u]:
                self._color[u] = not self._color[v]
                self._dfs(u)
            else:
                if self._color[u] == self._color[v]:
                    self._is_two_colorable = False

    def is_bipartite(self):
        return self._is_two_colorable


class SymbolGraph:

    def __init__(self):
        self._st = {}
        self._keys = None
        self._graph = None

    def load(self, filename, delim):
        with open(filename, 'r') as reader:
            lines = reader.readlines()

        for line in lines:
            for rv in line.split(delim):
                if rv not in self._st:
                    size = len(self._st)
                    self._st[rv] = size

        self._keys = [None] * len(self._st)
        for name in self._st:
            self._keys[self._st[name]] = name

        print(self._keys)

        self._graph = Graph(len(self._st))
        for line in lines:
            vs = line.split(delim)
            v = self._st[vs[0]]
            for u in vs[1:]:
                self._graph.add_edge(v, self._st[u])

    def contains(self, s):
        return s in self._st

    def index(self, s):
        return self._st.get(s)

    def name(self, v):
        return self._keys[v]

    def G(self):
        return self._graph


def test_path(v):
    G = Graph()
    G.load('tinyCG.txt')
    print(G)

    P = BFP(G, v)
    for x in range(G.vertex()):
        if P.has_path_to(x):
            path = '-'.join(map(str, P.path_to(x)))
        else:
            path = ''
        print('{} to {}: {}'.format(v, x, path))


def test_search(v):
    G = Graph()
    G.load('tinyG.txt')

    search = DFS(G, v)
    for x in range(G.vertex()):
        if search.connected(x) and v != x:
            print('{} - {}'.format(v, x))


def test_cc():
    G = Graph()
    G.load('tinyG.txt')

    cc = CC(G)
    print('id =>', cc._id)
    print('marked =>', cc._marked)
    print(cc.count())


def test_symbol_graph():
    sg = SymbolGraph()
    sg.load('routes.txt', ' ')

    print(sg.G())


if __name__ == "__main__":
    # test_search(9)
    # test_path(0)
    # test_cc()
    test_symbol_graph()
