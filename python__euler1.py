'''
If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
B = 1000
#setup sieve
multiples_board = []
for i in range(1,B+2): # off by one by adding
    multiples_board.append(None)
basket = list(range(1,B+1))
#pass 3
i = 0
while 3*i <= len(multiples_board)-2:
    multiples_board[3*i] = True
    i += 1
j = 0
while 5*j <= len(multiples_board)-2:
    multiples_board[5*j] = True
    j += 1

sum__ = 0
for m in range(1,B+1):
    if multiples_board[m] == True:
        sum__ += m
print(sum__)
