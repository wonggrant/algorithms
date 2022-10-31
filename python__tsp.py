
'''
Set of vertices V
import itertools
p = permutation(V)
p[0] = origin__v

p[i], p[j]
p[i] = 0
p[j] =

N = |V|
if j == N: break

i, j = 0, i+1
path_total__ = 0
while True:
    v__1,v__2 = p[i],p[j]
    if (v__1,v__2)  
    if j == N:
        break
    else:
        i,j = i+1, j+1
'''

set_of__vertices = {}
set_of__edges = {}
edge_to_distance__map = dict()
N,M = len(set_of__vertices), len(set_of__edges)
pos_inf = 2**(2**(2**2))
current_minimum_total_distance = pos_inf
current_minimal_full_path = None
import itertools
for path_minus_return in itertools.permutations(set_of__vertices):
    i,j = 0,1
    current_path_total_distance = 0
    current_path = []
    invalid__edge__found = None
    while True:
        v__1,v__2 = path_minus_return[i],path_minus_return[j]
        edge__ = (v__1,v__2)
        if edge__ in set_of__edges:
            current_path.append(edge__)
            current_path_total_distance += edge_to_distance__map[edge__]
            if j == N:
                v__3 = v__1
                return_to_origin__edge = (v__2,v__3)
                if return_to_origin__edge in set_of__edges:
                    current_path.append(edge__)
                    current_path_total_distance += edge_to_distance__map[return_to_origin__edge]
                else:
                    return_to_origin_edge_dne = True
                    break
        else:
            invalid__edge__found = True
            break
        i += 1
        j += 1
    if invalid__edge__found == True:
        continue
    if return_to_origin_edge_dne == True:
        continue
    if current_path_total_distance < current_minimum_total_distance:
        current_minimal_full_path = current_path
        current_minimum_total_distance = current_path_total_distance
print('minimum distance full walk', current_minimum_total_distance)
print('full walk', current_minimal_full_path)
        
    
