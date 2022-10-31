set_of_edges = {}
map_edge_weight = dict()
set_of_vertices = {}

V__ = len(set_of_vertices)

pos_inf = 2**(2**(2**2))
minimum_weight = pos_inf
minimum_spanning_tree = None
import itertools
# every MST has |V|-1 edges
for p in itertools.combinations(set_of_edges, V__ - 1):
    current_total = 0
    for e in p:
        current_total += map_edge_weight[e]
    if current_total < minimum_weight:
        minimum_spanning_tree = p
        minimum_weight = current_total
print('MST', minimum_spanning_tree, 'weight', minimum_weight)

