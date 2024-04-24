import random

DEBUG_PRINT = False
DEBUG_ONLY_TEST = "golomb"

TEST_RANDOM = True

def verify_clique(test_clique, edges):
    test_clique = list(test_clique)
    test_clique.sort()

    for c in test_clique:
        for t in test_clique:
            if c <= t:
                continue

            has_edge = False
            for e in edges:
                if (t, c) == e:
                    has_edge = True
                    break

            if not has_edge:
                return False

    return True

# nodes is a set of nodes, unique ID's
# edges is a set of a 2-tuple of (node_id_1, node_id_2) where the ids are not the same
#  -- edges are assumed to be: node_id_1 < node_id_2
def enumerate_cliques(nodes, edges, return_info=False):
    # 0) initialise graph data structures
    neighbours = {}
    node_edges = {}
    for n in nodes:
        for e in edges:
            in_edge = n in e
            if not in_edge:
                continue

            neighbour_list = neighbours.get(n, set([n]))
            neighbour_list.add(e[0])
            neighbour_list.add(e[1])
            neighbours[n] = neighbour_list

            edge = node_edges.get(n, [])
            edge.append(e)
            node_edges[n] = edge

    if DEBUG_PRINT:
        print("neighbours")
        for n, neighbour in neighbours.items():
            print(n, neighbour)

    # 1) report neighbours to edges
    edge_neighbour_reports = {}
    for n in nodes:
        for e in node_edges[n]:
            reports = edge_neighbour_reports.get(e, [])
            reports.append(neighbours[n])
            edge_neighbour_reports[e] = reports

    if DEBUG_PRINT:
        print()
        print("edge reports")
        for e, r in edge_neighbour_reports.items():
            print(e, r)

    # 2) intersect edge reports to get common neighbours
    edge_neighbour_intersections = {}
    for edge, reports in edge_neighbour_reports.items():
        intersections = reports[0].intersection(reports[1])
        edge_neighbour_intersections[edge] = intersections

    if DEBUG_PRINT:
        print()
        print("edge intersections")
        for e, i in edge_neighbour_intersections.items():
            print(e, i)

    # 3) create common neighbours for all nodes
    common_neighbours = {}
    for n in nodes:
        for edge in node_edges[n]:
            cn = common_neighbours.get(n, [])
            cn.append(edge_neighbour_intersections[edge])
            common_neighbours[n] = cn

    if DEBUG_PRINT:
        print()
        print("common neighbours")
        for n, cn in common_neighbours.items():
            print(n, cn)

    # 4) create common edges for all nodes
    meta_common_edges = []
    common_edges = {}
    for n in nodes:
        e = []
        for neighbour in neighbours[n]:
            if n == neighbour:
                continue
            for a in common_neighbours[n]:
                for b in common_neighbours[neighbour]:
                    common_edge = a.intersection(b)
                    if n in common_edge and neighbour in common_edge:
                        ce = common_edges.get(n, set())
                        ce.add(tuple(common_edge))
                        common_edges[n] = ce
                        e.append(common_edge)
        meta_common_edges.append(e)

    if DEBUG_PRINT:
        print()
        print("common edges")
        for n, ce in common_edges.items():
            print(n, ce)

    # 5) consolodate common edges to find cliques
    cliques = set()
    for n in nodes:
        while len(common_edges[n]) > 0:
            c = common_edges[n].pop()
            clique = set([n])
            for neighbour in neighbours:
                if n == neighbour:
                    continue
                if c in common_edges[neighbour]:
                    clique.add(neighbour)
                    common_edges[neighbour].remove(c)

            cliques.add(tuple(clique))

    # Return maximal cliques:
    #  if clique_i is subset of clique_j, |clique_j| > |clique_i|, we remove it
    cliques_to_remove = []
    for i in cliques:
        for j in cliques:
            if len(j) > len(i) and set(i).issubset(set(j)):
                cliques_to_remove.append(i)
                break

    for c in cliques_to_remove:
        cliques.remove(c)


    max_clique_size = 0
    max_cn_size = 0
    max_ce_size = 0

    for c in cliques:
        max_clique_size = max(max_clique_size, len(c))

    for n, cn in common_neighbours.items():
        max_cn_size = max(max_cn_size, len(cn))

    for ce in meta_common_edges:
        max_ce_size = max(max_ce_size, len(ce))

    if return_info:
        return (cliques, max_clique_size, max_cn_size, max_ce_size)
    else:
        return cliques

def k2():
    return (
        [1, 2],
        [(1, 2)]
    )

def k3():
    return (
        [1, 2, 3],
        [(1, 2), (1, 3), (2, 3)]
    )

def k4():
    return (
        [1, 2, 3, 4],
        [
            (1, 2), (1, 3), (1, 4),
            (2, 3), (2, 4),
            (3, 4)
        ]
    )

def k5():
    return (
        [1, 2, 3, 4, 5],
        [
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 3), (2, 4), (2, 5),
            (3, 4), (3, 5),
            (4, 5)
        ]
    )

def k6():
    return (
        [1, 2, 3, 4, 5, 6],
        [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
            (2, 3), (2, 4), (2, 5), (2, 6),
            (3, 4), (3, 5), (3, 6),
            (4, 5), (4, 6),
            (5, 6)
        ]
    )

def k7():
    return (
        [1, 2, 3, 4, 5, 6, 7],
        [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
            (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (3, 4), (3, 5), (3, 6), (3, 7),
            (4, 5), (4, 6), (4, 7),
            (5, 6), (5, 7),
            (6, 7)
        ]
    )

def kn(n):
    vertices = list(range(1,n + 1))
    edges = []
    for a in vertices:
        for b in vertices:
            if a >= b:
                continue

            edges.append((a, b))

    return (vertices, edges)

def disconnected_test():
    return (
        [1, 2, 3, 4, 5, 6],
        [
            (1, 2), (1, 3), (2, 3),
            (4, 5), (4, 6), (5, 6),
        ]
    )

def basic_test():
    return (
        [1, 2, 3, 4, 5],
        [(1, 2), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]
    )

def known_test():
    return (
        [1, 2, 3, 4, 5, 6],
        [
            (1, 2), (1, 5),
            (2, 3), (2, 5),
            (3, 4),
            (4, 5), (4, 6)
        ]
    )

def known_test_2():
    return (
        [1, 2, 3, 4, 5, 6],
        [
            (1, 2), (1, 4), (1, 5),
            (2, 3), (2, 5),
            (3, 4), (3, 5), (3, 6),
            (4, 5), (4, 6),
            (5, 6)
        ]
    )

def compliment_7path():
    return (
        [1, 2, 3, 4, 5, 6, 7],
        [
            (1, 2), (1, 3), (1, 4), (1, 6),
            (2, 3), (2, 5), (2, 7),
            (3, 4), (3, 5),
            (4, 5), (4, 6), (4, 7),
            (5, 6), (5, 7),
            (6, 7)
        ]
    )

def k5_k3():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8],
        [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (5, 6), (6, 7), (6, 8), (7, 8)]
    )

def petersen():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [
            (1, 2), (1, 5), (2, 3), (3, 4), (4, 5),
            (1, 6), (2, 7), (3, 8), (4, 9), (5, 10),
            (6, 8), (6, 9), (7, 10), (7, 9), (8, 10)
        ]
    )

def bidiakis_cube():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [
            (1, 4), (1, 2), (4, 5),
            (2, 5), (2, 3), (5, 6),
            (3, 6),
            (1, 7), (4, 9), (3, 10), (6, 12),
            (7, 10), (7, 8), (10, 11),
            (8, 11), (8, 9), (11, 12),
            (9, 12)
        ]
    )

def bull_graph():
    return (
        [1, 2, 3, 4, 5],
        [
            (1, 3), (2, 4),
            (3, 4), (4, 5), (3, 5)
        ]
    )

def diamond_graph():
    return (
        [1, 2, 3, 4],
        [
            (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)
        ]
    )

def square_graph():
    return (
        [1, 2, 3, 4],
        [
            (1, 2), (1, 4), (2, 3), (3, 4)
        ]
    )

def butterfly_graph():
    return (
        [1, 2, 3, 4, 5],
        [
            (1, 2), (1, 3), (2, 3),
            (1, 4), (1, 5), (4, 5)
        ]
    )

def chvatal_graph():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [
            (1, 2), (1, 4), (2, 3), (3, 4),
            (1, 5), (1, 12), (2, 6), (2, 7), (3, 8), (3, 9), (4, 10), (4, 11),
            (5, 6), (5, 8), (5, 9),
            (6, 10), (6, 11),
            (7, 8), (7, 10), (7, 11),
            (8, 12),
            (9, 10), (9, 12),
            (11, 12)
        ]
    )

def franklin_graph():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [
            (1, 6), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
            (1, 8), (2, 9), (3, 10), (4, 11), (5, 12), (6, 7),
            (7, 8), (9, 10), (11, 12)
        ]
    )

def errera_graph():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [
            (1, 3), (1, 2), (1, 4), (1, 5), (1, 9),
            (2, 5), (2, 6), (2, 7), (2, 3),
            (3, 7), (3, 8), (3, 9),
            (4, 5), (4, 10), (4, 11), (4, 9),
            (5, 6), (5, 11),
            (6, 7), (6, 11), (6, 12), (6, 13),
            (7, 8), (7, 13), (7, 14),
            (8, 9), (8, 10), (8, 15), (8, 16),
            (9, 10),
            (10, 11), (10, 16), (10, 17),
            (11, 12), (11, 17),
            (12, 13), (12, 17), (12, 18),
            (13, 14), (13, 15), (13, 18),
            (14, 15),
            (15, 16), (15, 18),
            (16, 17), (16, 18),
            (17, 18)
        ]
    )

def golomb_graph():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [
            (1, 3), (1, 2), (2, 3), (2, 6), (3, 8),
            (1, 4), (4, 5), (4, 9), (4, 10),
            (5, 6), (5, 10),
            (6, 7), (6, 10),
            (7, 8), (7, 10),
            (8, 9), (8, 10),
            (9, 10)
        ]
    )

def moser_spindle():
    return (
        [1, 2, 3, 4, 5, 6, 7],
        [
            (1, 2), (1, 5), (1, 6), (1, 7),
            (2, 3), (2, 7),
            (3, 4), (3, 7),
            (4, 5), (4, 6),
            (5, 6)
        ]
    )

def path_graph():
    return (
        [1, 2, 3, 4, 5, 6, 7],
        [ (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7) ]
    )

def wagner_graph():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8],
        [
            (1, 2), (1, 8), (1, 5),
            (2, 3), (2, 6),
            (3, 4), (3, 7),
            (4, 5), (4, 8),
            (5, 6), (6, 7), (7, 8)
        ]
    )

def wiener_araya_graph():
    return (
        [
             1,  2,  3,  4,  5,  6,
             7,  8,  9, 10, 11, 12,
            13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42
        ],
        [
            (1, 4), (1, 2), (1, 5), (1, 16),
            (2, 3), (2, 7), (2, 8),
            (3, 4), (3, 10), (3, 11),
            (4, 13), (4, 14),
            (5, 6), (5, 17),
            (6, 7), (6, 19),
            (7, 21),
            (8, 9), (8, 22),
            (9, 10), (9, 24),
            (10, 26),
            (11, 12), (11, 27),
            (12, 13), (12, 29),
            (13, 31),
            (14, 15), (14, 32),
            (15, 16), (15, 34),
            (16, 36),
            (17, 18), (17, 36),
            (18, 19), (18, 37),
            (19, 20),
            (20, 21), (20, 38),
            (21, 22),
            (22, 23),
            (23, 24), (23, 38), (23, 39),
            (24, 25),
            (25, 26), (25, 42),
            (26, 27),
            (27, 28),
            (28, 29), (28, 42),
            (29, 30),
            (30, 31), (31, 41),
            (31, 32),
            (32, 33),
            (33, 34), (33, 41), (33, 40),
            (34, 35),
            (35, 36), (35, 37),
            (37, 38), (37, 40),
            (39, 40), (39, 42),
            (41, 42)
        ]
    )

def goldner_harary_graph():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        [
            (1, 4), (1, 2), (1, 3), (1, 5), (1, 6), (1, 7), (1, 8), (1, 11),
            (2, 3), (2, 6),
            (3, 4), (3, 5), (3, 6), (3, 9), (3, 10), (3, 11),
            (4, 5),
            (5, 7), (5, 10), (5, 11),
            (6, 8), (6, 9), (6, 11),
            (7, 11),
            (8, 11),
            (9, 11),
            (10, 11)
        ]
    )

def sat_reduce():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [
            (1, 4), (1, 5), (1, 6), (1, 7),
            (2, 5), (2, 6), (2, 8), (2, 9),
            (3, 5), (3, 6), (3, 8), (3, 9),
            (4, 7), (4, 8), (4, 9),
            (5, 7),
            (6, 7),
        ]
    )

def k5_k4_killer_1():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [
            (1, 2), (1, 3), (1, 4), (1, 5),
            (1, 10), (1, 9), (1, 8),
            (2, 3), (2, 4), (2, 5),
            (2, 9), (2, 8), (2, 7),
            (3, 4), (3, 5),
            (3, 6), (3, 7), (3, 8),
            (4, 5),
            (4, 6), (4, 7), (4, 10),
            (5, 10), (5, 9), (5, 6),
            (6, 10), (6, 7),
            (7, 8),
            (8, 9),
            (9, 10)
        ]
    )

def k5_k4_killer_2():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [
            (1, 2), (1, 3), (1, 4), (1, 5),
            (1, 10), (1, 9), (1, 8), (1, 7),
            (2, 3), (2, 4), (2, 5),
            (2, 9), (2, 8), (2, 7), (2, 6),
            (3, 4), (3, 5),
            (3, 6), (3, 7), (3, 8), (3, 10),
            (4, 5),
            (4, 6), (4, 7), (4, 10), (4, 9),
            (5, 10), (5, 9), (5, 6), (5, 8),
            (6, 10), (6, 7),
            (7, 8),
            (8, 9),
            (9, 10)
        ]
    )

def star_killer():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [
            (1, 2), (1, 3), (1, 4), (1, 5),
            (1, 6), (1, 15), (1, 12), (1, 10),
            (2, 3), (2, 4), (2, 5),
            (2, 6), (2, 7), (2, 11), (2, 13),
            (3, 4), (3, 5),
            (3, 7), (3, 8), (3, 12), (3, 14),
            (4, 5),
            (4, 13), (4, 8), (4, 9), (4, 15),
            (5, 14), (5, 9), (5, 10), (5, 11)
        ]
    )

def k5_5k5_killer():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [
            (1, 2), (1, 3), (1, 4), (1, 5),
            (1, 6), (1, 7), (1, 9), (1, 10),
            (2, 3), (2, 4), (2, 5),
            (2, 6), (2, 7), (2, 8), (2, 10),
            (3, 4), (3, 5),
            (3, 6), (3, 7), (3, 8), (3, 9),
            (4, 5),
            (4, 7), (4, 8), (4, 9), (4, 10),
            (5, 6), (5, 8), (5, 9), (5, 10)
        ]
    )

def k5_2_killer():
    return (
        [1, 2, 3, 4, 5, 6],
        [
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 3), (2, 4), (2, 5),
            (3, 4), (3, 5),
            (4, 5),
            (1, 6), (2, 6), (3, 6), (5, 6)
        ]
    )

def random_graph_from_params(max_vertices):
    vertices = list(range(1, max_vertices))
    edges = set()
    for n in vertices:
        neighbours = random.sample(vertices, random.randrange(2, len(vertices)))
        for c in neighbours:
            if n == c:
                continue
            edge = (min(n, c), max(n, c))
            edges.add(edge)

    return (
        vertices,
        list(edges)
    )

# https://arxiv.org/abs/1504.06890
def tpd_refute():
    return (
        [1, 2, 3, 4, 5, 6, 7],
        [
            (1, 2), (1, 3), (1, 4), (1, 6),
            (2, 3), (2, 5), (2, 7),
            (3, 4), (3, 5),
            (4, 5), (4, 6), (4, 7),
            (5, 6), (5, 7),
            (6, 7)
        ]
    )

# https://arxiv.org/abs/1504.06890
def laplante_refute_1():
    return (
        #---------------A--B--C--D--E---F---G---H---I---J
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11),
            (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 12), (2, 13), (2, 14),
            (3, 4), (3, 5), (3, 6), (3, 9), (3, 15), (3, 12), (3, 13),
            (4, 5), (4, 7), (4, 11), (4, 14), (4, 9), (4, 12), (4, 15),
            (5, 8), (5, 10), (5, 11), (5, 14), (5, 15), (5, 13),
        ]
    )

# https://arxiv.org/abs/1504.06890
def laplante_refute_2():
    return (
        [1, 2, 3, 4, 5, 6, 7],
        [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
            (2, 3),
            (4, 5),
            (6, 7)
        ]
    )

# https://arxiv.org/abs/1504.06890
def laplante_refute_3():
    return (
        [1, 2, 3, 4],
        [
            (1, 2), (1, 3), (1, 4),
            (2, 3), (2, 4),
            (3, 4)
        ]
    )

# https://arxiv.org/abs/1504.06890
def laplante_refute_4():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
        [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
            (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19),
            (1, 20), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (1, 26), (1, 27), (1, 28),
            (1, 29), (1, 30), (1, 31), (1, 32), (1, 33), (1, 34), (1, 35), (1, 36), (1, 37),
            (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17),
            (18, 19), (20, 21), (22, 23), (24, 25), (26, 27), (28, 29), (30, 31), (32, 33),
            (34, 35), (36, 37)
        ]
    )

# https://arxiv.org/abs/1504.06890
def laplante_refute_5():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
        [
            (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
            (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19),
            (1, 20), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (1, 26), (1, 27), (1, 28),
            (1, 29), (1, 30), (1, 31), (1, 32), (1, 33), (1, 34), (1, 35), (1, 36), (1, 37),
            (2, 3), (4, 5), (6, 7), (8, 9), (12, 13), (14, 15), (16, 17),
            (18, 19), (20, 21), (22, 23), (24, 25), (26, 27), (28, 29), (30, 31), (32, 33),
            (34, 35), (36, 37), (32, 34), (33, 34)
        ]
    )

# Cazals, Frederic & Karande, Chinmay. (2006). Reporting maximal cliques: new insights into an old problem. Tech rep INRIA.
def exp_cliques():
    return (
        [1, 2, 3, 4, 5, 6, 7, 8],
        [
            (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
            (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 5), (3, 6), (3, 7), (3, 8),
            (4, 5), (4, 6), (4, 7), (4, 8),
            (5, 7), (5, 8),
            (6, 7), (6, 8),
        ]
    )

def random_graph():
    return random_graph_from_params(random.randrange(4, 50))

def pretty_print_cliques(cliques):
    max_clique_size = 0
    for c in cliques:
        max_clique_size = max(max_clique_size, len(c))
    max_clique_size = max_clique_size + 1

    for i in range(2, max_clique_size):
        ki = { c for c in cliques if len(c) == i }
        print(f"k{i}: {ki}")

def test_graph(nodes, edges):
    cliques = enumerate_cliques(nodes, edges)
    for c in cliques:
        if not verify_clique(c, edges):
            print("Invalid clique:", c)
    cliques = { c for c in cliques if verify_clique(c, edges) }
    pretty_print_cliques(cliques)

def main():
    graphs = [
        ("k2", k2()),
        ("k3", k3()),
        ("k4", k4()),
        ("k5", k5()),
        ("k6", k6()),
        ("k7", k7()),
        ("k30", kn(30)),
        ("disconnected", disconnected_test()),
        ("basic", basic_test()),
        ("known", known_test()),
        ("known_2", known_test_2()),
        ("compliment_7path", compliment_7path()),
        ("k5_k3", k5_k3()),
        ("petersen", petersen()),
        ("bidakis_cube", bidiakis_cube()),
        ("bull", bull_graph()),
        ("diamond", diamond_graph()),
        ("square", square_graph()),
        ("butterfly", butterfly_graph()),
        ("cvhatal", chvatal_graph()),
        ("franklin", franklin_graph()),
        ("errera", errera_graph()),
        ("golomb", golomb_graph()),
        ("moser", moser_spindle()),
        ("path", path_graph()),
        ("wagner", wagner_graph()),
        ("wiener_araya_graph", wiener_araya_graph()),
        ("goldner_harary", goldner_harary_graph()),
        ("tpd_refuse", tpd_refute()),
        ("laplante_refute_1", laplante_refute_1()),
        ("laplante_refute_2", laplante_refute_2()),
        ("laplante_refute_3", laplante_refute_3()),
        ("laplante_refute_4", laplante_refute_4()),
        ("laplante_refute_5", laplante_refute_5()),
        ("sat_reduction_example", sat_reduce()),
        ("exp_cliques", exp_cliques()),
        ("k5_k4_killer_1", k5_k4_killer_1()),
        ("k5_k4_killer_2", k5_k4_killer_2()),
        ("star_killer", star_killer()),
        ("k5_5k5_killer", k5_5k5_killer()),
        ("k5_2_killer", k5_2_killer()),
    ]

    for name, (nodes, edges) in graphs:
        if DEBUG_PRINT and name != DEBUG_ONLY_TEST:
            continue
        print(f"Testing {name}")
        test_graph(nodes, edges)
        print('-'*90)

    # Used to test if we ever misreport a clique. Not to be used to show that maximal
    # cliques were found.
    if TEST_RANDOM:
        invalid_graphs = 0
        print("Testing random graphs...")
        for i in range(0, 100_000):
            is_report_iteration = (0 == ((i + 1) % 10))
            (nodes, edges) = random_graph()

            max_clique_size = 0
            max_cn_size = 0
            max_ce_size = 0
            cliques, max_clique_size, max_cn_size, max_ce_size = enumerate_cliques(nodes, edges, True)

            for c in cliques:
                if not verify_clique(c, edges):
                    print("Invalid clique:", c)

            print('-'*3, "DETAILS", '-'*3)
            vertex_count = len(nodes)

            if max_ce_size > vertex_count**3:
                invalid_graphs = invalid_graphs + 1

            print(f"|V| = {len(nodes)}")
            print(f"|E|_max: {vertex_count * (vertex_count - 1) // 2}")
            print(f"|E| = {len(edges)}")
            print(f"|cliques| = {len(cliques)}")
            print(f"max |CE| = {max_ce_size} <= {vertex_count**3} ({max_ce_size <= vertex_count**3})")
            print(f"max |CN| = {max_cn_size} <= {vertex_count - 1} ({max_cn_size <= vertex_count - 1})")
            print(f"max k-clique len = {max_clique_size}")
            print(f"Invalid Graph Count = {invalid_graphs}")

            print("Clique Counts: ", end="")
            max_clique_size = 0
            for c in cliques:
                max_clique_size = max(max_clique_size, len(c))
            for j in range(2, max_clique_size + 1):
                count = 0
                for c in cliques:
                    if len(c) == j:
                        count = count + 1
                print(f"K_{j} = {count} ", end="")
            print()

            if is_report_iteration:
                print(f"Tested {i + 1} graphs")
            else:
                print()

if __name__ == "__main__":
    main()
