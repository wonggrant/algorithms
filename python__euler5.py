'''
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without
any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
'''
'''
b = 10
smallest__ = 1
for k in range(1,b+1):
    smallest__ *= k
print(smallest__)
'''
b = 10
i = b
while True:
    not_divisible_found = None
    divisible_by_all = None
    for j in range(1,b+1):
        if i % j != 0:
            #print(i,j)
            not_divisible_found = True
            break
    if not_divisible_found == None:
        not_divisible_found = False
    if not_divisible_found == True:
        i += 1
    else:
        divisible_by_all = True
        break
print(i) # 2520
