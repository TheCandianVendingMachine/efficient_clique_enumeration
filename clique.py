import time

DEBUG_PRINT = False
DEBUG_ONLY_TEST = "cocktail_5"

LOG_SECTION_TIME = True

TEST_RANDOM = False

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
    total_t0 = time.time()
    if DEBUG_PRINT:
        print("edges")
        print(edges)
        print()

    # 0) initialise graph data structures
    t0 = time.time()
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
    if LOG_SECTION_TIME:
        print(f"Graph initialised in {time.time() - t0} seconds")

    # 1) report neighbours to edges
    t0 = time.time()
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
    if LOG_SECTION_TIME:
        print(f"Edge reports done in {time.time() - t0} seconds")

    # 2) intersect edge reports to get common neighbours
    t0 = time.time()
    edge_neighbour_intersections = {}
    for edge, reports in edge_neighbour_reports.items():
        intersections = reports[0].intersection(reports[1])
        edge_neighbour_intersections[edge] = intersections

    if DEBUG_PRINT:
        print()
        print("edge intersections")
        for e, i in edge_neighbour_intersections.items():
            print(e, i)
    if LOG_SECTION_TIME:
        print(f"Edge reports intersected in {time.time() - t0} seconds")

    # 3) create common neighbours for all nodes
    t0 = time.time()
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
    if LOG_SECTION_TIME:
        print(f"Common neighbours generated in {time.time() - t0} seconds")

    # 4) create common edges for all nodes
    t0 = time.time()
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
            print(n)
            for c in ce:
                print("\t", c)
    if LOG_SECTION_TIME:
        print(f"Common edges generated in {time.time() - t0} seconds")

    # 5) consolodate common edges to find cliques
    t0 = time.time()
    cliques = set()
    for n in nodes:
        cliques_to_add = set()
        max_clique_size = 0
        for c in common_edges[n]:
            clique = set([n])
            for neighbour in neighbours[n]:
                if n == neighbour:
                    continue
                for cen in common_edges[neighbour]:
                    i = set(cen).intersection(set(c))
                    if n in i and n in i:
                        clique = tuple(sorted(tuple(i)))
                        if len(clique) >= max_clique_size and verify_clique(clique, edges):
                            if len(clique) > max_clique_size:
                                max_clique_size = len(clique)
                                cliques_to_add.clear()
                            cliques_to_add.add(clique)

        cliques = cliques.union(cliques_to_add)

    if LOG_SECTION_TIME:
        print(f"All maximal cliques found in {time.time() - t0} seconds")

    max_clique_size = 0
    max_cn_size = 0
    max_ce_size = 0

    for c in cliques:
        max_clique_size = max(max_clique_size, len(c))

    for n, cn in common_neighbours.items():
        max_cn_size = max(max_cn_size, len(cn))

    for ce in meta_common_edges:
        max_ce_size = max(max_ce_size, len(ce))

    if LOG_SECTION_TIME:
        print(f"Enumerated cliques in {time.time() - total_t0} seconds")

    if return_info:
        return (cliques, max_clique_size, max_cn_size, max_ce_size)
    else:
        return cliques

from test_graphs import *

def test_graph(nodes, edges):
    (cliques, max_clique_size, max_cn_size, max_ce_size) = enumerate_cliques(nodes, edges, True)
    for c in cliques:
        if not verify_clique(c, edges):
            print("Invalid clique:", c)
    cliques = { c for c in cliques if verify_clique(c, edges) }
    pretty_print_cliques(cliques)

    print()
    vertex_count = len(nodes)
    edge_count = vertex_count * (vertex_count - 1) // 2
    print(f"|V| = {vertex_count}")
    print(f"|E|_max: {edge_count}")
    print(f"|E| = {len(edges)}")
    print(f"|cliques| = {len(cliques)}")
    print(f"max |CE| = {max_ce_size} <= {vertex_count**3} ({max_ce_size <= vertex_count**3})")
    print(f"max |CN| = {max_cn_size} <= {vertex_count - 1} ({max_cn_size <= vertex_count - 1})")
    print(f"max k-clique len = {max_clique_size}")

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
        ("cocktail_2", cocktail_graph(2)),
        ("cocktail_3", cocktail_graph(3)),
        ("cocktail_4", cocktail_graph(4)),
        ("cocktail_5", cocktail_graph(5)),
        ("cocktail_6", cocktail_graph(6)),
        ("cocktail_7", cocktail_graph(7)),
        ("cocktail_8", cocktail_graph(8)),
        ("cocktail_9", cocktail_graph(9)),
        ("cocktail_10", cocktail_graph(10)),
        ("cocktail_easier", cocktail_easier()),
        ("cocktail_kinda", cocktail_kinda()),
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

            edge_count = vertex_count * (vertex_count - 1) // 2
            print(f"|V| = {len(nodes)}")
            print(f"|E|_max: {edge_count}")
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
