# Algorithms

def find_inefficient(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return i
    return None

# N possible guesses
# Ask a yes or  no question
# N.2 possibles guesses [repeat]

# How many questions to get from N to 1?

# N                 2^k
# ...
# 4                 2^2
# 2                 2^1
# 1                 2^0

# N = 2^k => k = log2(N)

# 20 = log2(N)
# N = 2^20 = (2^10)^2 - (10^3)^2 = 1 million

def binary_search(L, e):
    '''Retunr the location of the element e
    in the sorted list of integers L'''

    low, high = 0, len(L) - 1

    # e is somewhere between L[low] and L[high]

'''   while       :
        mid = (low + high) // 2
        if e < L[mid]:
            high = mid - 1
        elif e > L[mid]:
            low = mid + 1
        else:
            return mid'''