'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import itertools
ans__product = None
ans__ = None
c__ = 0
while True:
    a__space, b__space = list(range(c__)), list(range(c__))
    print(a
    ans__found = False
    for p in itertools.product(a__space, b__space):
        a__,b__ = p[0], p[1]
        if a__**2 + b__**2 == c__**2 and a__ + b__ + c__ == 1000:
            ans__ = (a__,b__,c__)
            ans__product = a__ * b__ * c__
            ans__found = True
            break
        else:
            pass
    if ans__found == True:
        break
    c__ += 1
print(ans__, ans__product)
# (200, 375, 425) 31875000
