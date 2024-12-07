# Slow exponentiation

def slow_exponentiation(n):
    if n == 0:
        return 1
    else:
        return slow_exponentiation(n-1) + slow_exponentiation(n-1)

'''
        n-2 n-2    n-2  n-2
            n-1     n-1
                n

2^0 + 2^1 + 2^2 = (2^(n+1) -1)/(2-1) - 2^(n+1) = 2^2^n

O(2^n)
'''

# Sum of Lists

def sum_list2(L):
    '''Return the sum of the list of ints L'''
    if len(L) == 0:
        return 0
    
    if len(L) == 1:
        return L[0]  #the sum of the list is L[0] if L[0] is the only element
    
    mid = len(L)//2 #(the index of the approximate midpoint of the list)
    return sum_list2(L[:mid]) + sum_list2(L[mid:])

'''
     [1].......[1]...[1]....................[1]              
        .                                   .
         .                                 .
          .                               .
           .                             .
             .                          . 
             [n/4]    [n/4]  [n/4]  [n/4]
               \      /       \     /
                \    /         \   /
                 [n/2]        [n/2]
                   \          /
                    \        /
                     \      /
                      \    /
                        [n]

Total number of calls: 2^0 + 2^1 + ... + 2^(log2n)

= (2^(log2(n) + 1)) -1)/(2-1)
= 2^(log2(n)+1) = 2*2^(log2(n)) = 2n

O(n)
'''

[5, 6, 2, 10, 123, 2, 567]

# Mergesort idea
# split the input list L in half
# sort left half, sort right half
# merge the results


[2, 5, 6, 10]       [2, 123, 567]

[2, 2, 5, 6, 10, 123, 567]

def merge(L1, L2):
    '''Return the sorted version of L1 + L2
    L1 and L2 are sorted lists of integers'''

    # return sorted(L1+L2)

    res = []
    i1, i2 = 0, 0
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            res.append(L1[i1])
            i1+= 1
        else:
            res.append(L1[i2])
            i2+= 1

    res.extend(L1[i1:])
    res.extend(L2[i2:])

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    

    
    mid = len(L)//2
    return merge_sort(L[:mid]), merge_sort(L[mid:])