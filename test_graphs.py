import random

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

def cocktail_graph(n):
    vertices = list(range(1, 2 * n + 1))
    edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, 2 * n + 1):
            if j == n + i:
                continue
            edges.append((i, j))

    for i in range(n + 1, 2 * n + 1):
        for j in range(i + 1, 2 * n + 1):
            edges.append((i, j))

    return (vertices, edges)

def cocktail_easier():
    max_k = 5
    g1_vertices, g1_edges = kn(max_k)
    g2_vertices, g2_edges = kn(max_k)
    g2_vertices = [v + max_k for v in g2_vertices]
    g2_edges = [(v1 + max_k, v2 + max_k) for v1, v2 in g2_edges]

    # If x == y == max_k, then this is equivalent to cocktail_(max_k)
    x = 4
    y = 5
    k4_edges = []
    for i in range(0, x):
        for j in range(0, y):
            if i == j:
                continue
            k4_edges.append((g1_vertices[i], g2_vertices[j]))

    return (
        g1_vertices + g2_vertices,
        g1_edges + g2_edges + k4_edges
    )

def cocktail_kinda():
    max_k = 5
    g1_vertices, g1_edges = kn(max_k - 1)
    g2_vertices, g2_edges = kn(max_k)
    g2_vertices = [v + max_k for v in g2_vertices]
    g2_edges = [(v1 + max_k, v2 + max_k) for v1, v2 in g2_edges]

    k4_edges = []
    for i in range(0, len(g1_vertices)):
        for j in range(0, len(g2_vertices)):
            if i == j:
                continue
            k4_edges.append((g1_vertices[i], g2_vertices[j]))

    return (
        g1_vertices + g2_vertices,
        g1_edges + g2_edges + k4_edges
    )

def pretty_print_cliques(cliques):
    max_clique_size = 0
    for c in cliques:
        max_clique_size = max(max_clique_size, len(c))
    max_clique_size = max_clique_size + 1

    for i in range(2, max_clique_size):
        ki = { c for c in cliques if len(c) == i }
        print(f"k{i}: {ki}")
