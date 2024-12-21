# L = [1, 5, 7, 8, 9, 10, 11]

# low = 0 -> 4
# high = 6
# mid = 3 -> 5

def binary_search(L, e):
    low = 0
    high = len(L) -1
    #low is the loewst possible answer
    # high is the highest possible answer
    while low < high:
        mid = (low + high) // 2
        if L[mid] == e:
            return mid
        elif L[mid] < e:
            low = mid + 1
        else:
            high = mid - 1
    return low

# len(L) = n
# How many iterations of the loop does it take
# to get the answer?

# (high-low) is the size of the range of indices that we're looking at
# (high-low) decreases by at least a factor of 2 every iteration

# iteration 1: (high-low) ~ n
# iteration 2: (high-low) <= n/2
# iteration 3: (high-low) <= n/4
# ... 
# iteration k: done

# what is k?

# 1, 2, 4, 8, ...., n = 2^k
# k ~ log2(n)

# binary search for a list of size n requires at most
# log2(n) * c, wjere c is a constant

def linear_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return i
        
# How many interations does linear search take?
# In the worst case (when e is at L[-1])
# It takes time proportional to c2 * n, where n = len(L)

#Suppose that on my computer, c is 0.001 ms, c2, is 0.0001 

# for len(L) = 50

# linear search: 0.0001*50ms = 0.05 ms
# binary search: 0.001*log2(50) = 0.005 ms

# for len(L) = 50 million

# linear search = 5 000 ms
# binary search = 0.02 ms