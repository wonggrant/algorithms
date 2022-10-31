'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the
product of two 3-digit numbers.
'''
three_digit_numbers = list(range(100,999+1))
import itertools
neg_inf = -2**(2**(2**2))
current_largest_palidrome_product = neg_inf
first_term,second_term = None,None
for p in itertools.product(three_digit_numbers, three_digit_numbers):
    #print(p)
    a__,b__ = p[0],p[1]
    is_palidrome = None
    product__ = a__ * b__
    #print(product__)
    product__str = str(product__)
    #print(product__str)
    is_even_len = True if len(product__str) % 2 == 0 else False
    first_segment,second_segment = None, None
    N = len(product__str)
    if is_even_len == True:
        '''
        aaabbb len 6 / 2 = 3
        0123
        '''
        m__ = (N//2)
        first_segment = product__str[:m__]
        second_segment = product__str[m__:]
    else:
        '''
        aaabccc len 7 // 2 = 3
        0123456
        '''
        pivot__index = N//2
        first_segment = product__str[:pivot__index]
        second_segment = product__str[pivot__index+1:]
    is_palidrome = True if second_segment[::-1] == first_segment else False
    if is_palidrome == True:
        if product__ > current_largest_palidrome_product:
            print(product__)
            first_term, second_term = a__,b__
            current_largest_palidrome_product = product__
the_largest_palidrome_product__ = current_largest_palidrome_product
print(the_largest_palidrome_product__, first_term, second_term)
# 906609 913 993
