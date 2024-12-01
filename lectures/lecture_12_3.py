def print_list(L):
    if len(L) == 0:
        return
    print(L[0])
    print_list(L[1:])
'''
Call tree
[]

[3] -> 3

[2, 3] -> 2

[1, 2, 3] -> 1
'''
def print_list_reverse2(L):
    if len(L) == 0:
        return
    print_list_reverse2(L[1:])
    print(L[0])

def sum_list(L):
    '''Return the sum of the integers in the list L'''

    # Base case: List of 0 elements -> Sum = 0
    # Recursive Step: retun L[0] + sum_list(L[1:])

    if len(L) == 0:
        return 0

    return L[0] + sum_list(L[1:])

def sum_list2(L):
    if len(L) == 0:
        return 0

    if len(L) == 1:
        return L[0]

    mid = len(L) // 2
    return sum_list2(L[:mid]) + sum_list2(L[mid:])

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

'''
Runtime complexity of power?

Make n+1 calls
each call takes the same amount of time
(assuming * takes the same amount of time every time)
Let's say that amount is t1
For x a float, this assumption is correct

Total runetime: (n+1)*t1
proportional to n for large n
O(n)
'''

def power_fast(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    
    half_n = n//2
    half_power = power_fast(x, half_n)
    almost_full_power = half_power * half_power

    if n % 2 == 0:
        return almost_full_power
    else:
        return almost_full_power * x