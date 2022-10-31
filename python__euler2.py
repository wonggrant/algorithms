'''
Each new term in the Fibonacci sequence is generated
by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the
sum of the even-valued terms.
'''
fib_tape = [1, 2]
i, j = 0, 1
while True:
    fib__k = fib_tape[i] + fib_tape[j]
    if fib__k > 4000000:
        break
    fib_tape.append(fib__k)
    i, j = i+1,j+1
print(fib_tape)
sum__ = 0
for t in fib_tape:
    if t % 2 == 0:
        sum__ += t
print(sum__)
