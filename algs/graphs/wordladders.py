from collections import deque

from pygraph import Graph


def build_graph(word_file):
    d = {}
    g = Graph()

    with open(word_file, 'r') as reader:
        for line in reader:
            word = line.strip()
            for n in range(len(word)):
                bucket = word[:n] + '_' + word[n+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

    for bucket in d:
        for x in d[bucket]:
            for y in d[bucket]:
                if x != y:
                    g.add_edge(x, y)

    return g


def dfs(graph, start, target):
    vert_queue = deque()
    start_vert = graph.get_vertex(start)
    vert_queue.append(start_vert)
    while vert_queue:
        current = vert_queue.popleft()
        if current.get_id() == target:
            break
        for v in current.get_connections():
            if v.is_untraced():
                v.set_tracing()
                v.set_distance(current.get_distance() + 1)
                v.set_predecessor(current)
                vert_queue.append(v)
        current.set_traced()


def traverse(v):
    while v.get_predecessor():
        print(v.get_id())
        v = v.get_predecessor()
    print(v.get_id())


def print_graph(g):
    for v in g:
        for conn in v.get_connections():
            print("(%s, %s)" % (v.get_id(), conn.get_id()))


def slove_word_ladder(word_file, given, target):
    graph = build_graph(word_file)
    dfs(graph, given, target)
    v = graph.get_vertex(target)
    traverse(v)


if __name__ == "__main__":
    slove_word_ladder('words.txt', 'fool', 'sage')
