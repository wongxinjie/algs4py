import sys
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def build_heap(self, tuples):
        for rv in tuples:
            heapq.heappush(self._queue, rv)

    def delete_min(self):
        p, v = heapq.heappop(self._queue)
        return v

    def descrease_key(self, key, value):
        items = []
        while self._queue:
            p, v = heapq.heappop(self._queue)
            if v == key:
                p = value
            items.append((p, v))

        self.build_heap(items)

    def is_empty(self):
        return not self._queue


def dijkstra(graph, start):
    pq = PriorityQueue()
    for v in graph:
        v.set_distance(sys.maxsize)

    start.set_distance(0)
    pq.build_heap([(v.get_distance(), v) for v in graph])
    while not pq.is_empty():
        current_vert = pq.delete_min()
        for v in current_vert.get_connections():
            dist = current_vert.get_distance() + current_vert.get_weight(v)
            if dist < v.get_distance():
                v.set_distance(dist)
                v.set_predecessor(current_vert)
                pq.descrease_key(v, dist)
