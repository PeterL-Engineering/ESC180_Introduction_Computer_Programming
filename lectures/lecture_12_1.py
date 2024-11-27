# 5 000 000 books in robarts

[1, 10, 2, 1, 123, 4, 500, 2]

#[0, 2, 2, 0, 1, .. 1 , 0] # counts
#[0, 1, 2, 3, 4, ...10, 0]

'''
Counting Sorts: Construct a list of counts
count[i] is the number of times i appears
Reconstruct the sorted version of the list
using the counts:
[i]*counts[i] for every i
'''

def counting_sort(L):
    counts = [0] * (max(L) + 1) 
    # We need to be able to count the max number even if len(L) != max(L)
    # cl*max(L) + c2*len(L) time for some c1, c2
    # computing max(L) takes time prop. to len(L)
    # contructing list of max(L) elems takes time
    # prop. to max(L)

    # c*len(L) time
    for e in L:
        counts[e] += 1

    # c4*max(L) +c5*len(L)
    # the loop repeats max(L) times
    # we construct a list of size len(L) eventually

    res = []
    for i in range(len(counts)):
        res.extend([i] * counts[i])
    
    return res

# The total runtime of counting sort:
# (c1 + c4)*max(L) + (c2 + c3 + c5)*len(L)
# Complexity = 0(len(L)+max(L))
L = [1, 10, 2, 1, 4, 2]
counting_sort(L)

'''
Assumption in counting sort
Sorting non-negative integers
allows us to access counts[e] for every e

'''

# =======================================

# Recursion: Function calling itself

# n! = 1*2*3*..*n

def fact(n):

    if n == 0:
        return 1
    return n * fact(n-1)