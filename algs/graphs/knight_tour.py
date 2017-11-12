from pygraph import Graph


def pos_to_node_id(row, col, size):
    return row * size + col


def knight_graph(borad_size):
    graph = Graph()

    for row in range(borad_size):
        for col in range(borad_size):
            node_id = pos_to_node_id(row, col, borad_size)
            moves = get_legal_moves(row, col, borad_size)
            for p in moves:
                nid = pos_to_node_id(p[0], p[1], borad_size)
                graph.add_edge(node_id, nid)
    return graph


def get_legal_moves(x, y, size):
    moves = []
    offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
               (1, -2), (1, 2), (2, -1), (2, 1)]

    for p in offsets:
        x = x + p[0]
        y = y + p[1]
        if legal_coord(x, size) and legal_coord(y, size):
            moves.append(x, y)

    return moves


def legal_coord(x, size):
    return 0 <= x < size


def order_by_avail(vert):
    rvs = []
    for v in vert.get_connections():
        if v.is_untraced():
            c = 0
            for w in v.get_connections():
                if w.is_untraced():
                    c += 1
            rvs.append((c, v))
    rvs.sort(key=lambda x: x[0])
    return [rv[1] for rv in rvs]


def knight_tour(n, path, u, limit):
    u.set_tracing()
    path.append(u)
    if n < limit:
        # neighbor_list = list(u.get_connections())
        neighbor_list = order_by_avail(u)
        i = 0
        done = False
        while i < len(neighbor_list) and not done:
            if neighbor_list[i].is_untraced():
                done = knight_tour(n+1, path, neighbor_list[i], limit)
            i += 1
        if not done:
            path.pop()
            u.set_untraced()
    else:
        done = True
    return done
