'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
sum__ = 2
slots = [{},{},{2}]
print("2")
current_slot = 2
while current_slot < 2000000:
    for j in range(5):
        slots.append(set())
    current_slot_prime_factors = slots[current_slot]
    if current_slot_prime_factors == set():
        i = current_slot
        print(i)
        sum__ += i
        slots[current_slot+current_slot] = slots[current_slot+current_slot].union(set({current_slot}))
    else:
        for f in current_slot_prime_factors:
            slots[current_slot+f] = slots[current_slot+f].union(set({f}))
    current_slot += 1
print(sum__)
# 142913828922
