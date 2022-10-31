items = ['blue', 'red', 'yellow', 'grey', 'green']
weights = [2, 1, 4, 1, 12]
values = [2, 1, 10, 2, 4]

# corresponding from given problem input

knapsack_capacity = 15
max_quantities = []
for w_i in weights:
    quantity_i = 0
    while quantity_i * w_i <= knapsack_capacity - w_i:
        quantity_i += 1
    max_quantities.append(quantity_i)

print(items)
print('weights', weights)
print(values)
print(knapsack_capacity)
print('max quantities', max_quantities)

# max possible number of only one item_i

import itertools

possible_quantities = []
for max_q_i in max_quantities:
    possible_quantities.append(list(range(0, max_q_i +1)))

print(possible_quantities)

neg_inf = -2**(2**(2**(2**2)))
best_item_quantities = None
best_value = neg_inf
best_weight = None
for item_quantities in itertools.product(*possible_quantities):
    current_selection_total_weight = 0
    current_selection_total_value  = 0
    feasible = None
    for i, q in enumerate(item_quantities):
        current_selection_total_weight += q * weights[i]
        current_selection_total_value += q * values[i]
        if current_selection_total_weight > knapsack_capacity:
            feasible = False
            break
    if feasible == False:
        pass
    if feasible == None:
        feasible = True
    if feasible == True:
        if current_selection_total_value > best_value:
            best_item_quantities = item_quantities
            best_value = current_selection_total_value
            best_weight = current_selection_total_weight
        else:
            pass

print('best item quantities', best_item_quantities)
print('best value', best_value)
print('best_weight', best_weight)
        
            





    
