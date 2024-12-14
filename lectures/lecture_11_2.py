import matplotlib as plt
import time

def linear_search(L, e):
    for i in range(L, e):
        if L[i] == e:
            return i

def quadratic_search(L, e):
    for i in range(len(L)**2):
        pass

def timeit(f, arg1, arg2):
    '''Return the runtime of f(arg1, arg2)'''
    n_runs = 1000 
    for i in range(n_runs):
        start_t = time.time() #amt of seconds since Jan 1 1980

    for i in range(n_runs):
        f(arg1, arg2)
    end_t = time.time()
    return (end_t - start_t)/n_runs

print(timeit(linear_search, [0]*10000, 1))

lengths = [0, 1, 10, 100, 1000, 10000]
runtimes = []
runtimes_sq = []
for length in lengths:
    runtimes.append(timeit(linear_search, [0]*length, 1))
    runtimes.append(timeit(quadratic_search, [0]*length, 1))

plt.plot(lengths, runtimes)
plt.show()

#==================================================

# Nested Loop Efficiency

def f(m, n):
    for i in range(n):
        for j in range(m):
            pass

def g(n):
    for i in range(n):
        for j in range(n//2):
            pass

# Complexity of f?
# The runtime is proportional to the number of iterations
# What's the number of iterations (m*n)
# Ie. O(m*n)

# Complexity of g?
# The runtime is still proportional to the number of iterations
# How many iteratinos? n*(n/2) = (n^2)/2
# Ie. O(n^2)

'''
For project 3, look at each sentence and count co-occurences,
then look at the next sentence, [...]. You still have a nested loop, 
but you're only looking over the maximum length being the longest sentence.

m = number of sentences
k is the longest possible sentence

for sentence in sentences:
    for word in sentence:
        for word2 in sentnece:
            #update d[word1][word2]

            O = (m*k^2)
'''