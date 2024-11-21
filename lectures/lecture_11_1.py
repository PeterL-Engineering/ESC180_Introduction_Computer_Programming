
'''
I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.
However, I know nothing at all about my disease, and do not know for certain what ails me.

The word “man” only appears in the first three sentences. Its semantic descriptor vector would be:
{"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}
The word “liver” only occurs in the second sentence, so its semantic descriptor vector is:
{"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}'''

#               i am a sick spiteful an unattractive believe my is diseased ....
#"man":         3  3 2  1       1     1      1            0   0  0     0
#"liver":       1  0 0  0       0     0      0            1   1  1     1
#"spiteful":    
#"believe":     

# constrct an n-dimensional vector that corresponds to each word in the corpus
# n is the number of vectors as 

# More About Complexity

def find_e(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return i
    return -1

# To measure how efficient the function is:
# In the worst case (ie. if we don't return early), what is the
# runtime proportional to?

# For find_e: runtime is proprtional to n, where n = len(L)

# For binary search, the runtime is prportional to log2(n)

# For a linear search, even if runtime 0.*n ms, and binary is 1000*log2(n)
# it is still better to choose binary

# The worst-case asymptotic runtime complexity of find e
# is O(n), for n = len(L) * O = Order

'''Rigorous definition for complexity

g(n) if O(f(n)) if lim sup      g(n)/f(n) < c
                    n -> infty
informally: g grows at most as fast as f <=> g(n)f(n) does ont go to infinity

sup is aka least upper bound

lin sup h(n) = lin              [l.u.b h(k)]
n -> infty     n -> infty           k >= n

Runtime: g(n): the runtime for input of size n
f(n): complexity'''