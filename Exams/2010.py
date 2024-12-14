'''
Q. 4 Write a function add_neighbours that takes a list of integers and returns a new list, with the same number
of elements as the original list but where each integer in the new list is the sum of its neighbours and itself
(from the original list). For example, add_neighbours([1,3,5,7]) returns [4,9,15,12] (which is equal
to [1+3, 1+3+5, 3+5+7, 5+7]).
'''

def add_neighbours(L):
    if len(L) <= 1:
        return L
    elif len(L) == 2:
        L[0] += L[1]
        L[1] = L[0]
        return L
    else:
        second = L[1]
        second_last = L[-2]
        for i in range(1, len(L) - 1):
            L[i] += L[i - 1] + L[i + 1]
        
        L[0] += second
        L[-1] += second_last

        return L
    
'''
Q. 5 Write a function difference that takes two dictionaries d1, d2 and that returns a third dictionary d such
that d contains every key that appears in both d1 and d2 but with different values (i.e., where the values
d1[key] and d2[key] are different). For each such key, you should set the value of d[key] to the tuple
(d1[key], d2[key]). For example, if
d1 = { "a": 1, "b": 2, "c": 3 }
d2 = { "b": 2, "c": 4, "d": 6 }
then difference(d1, d2) returns { "c": (3,4) }.
'''

def difference(d1, d2):
    res = {}

    for key in d1.keys():
        if key in d2:
            res[key] = (d1[key, d2[key]])

    return res

'''
Q, 7 Write a function flatten that takes a list L and that returns a list of all non-list elements nested within
L, no matter how many sub-lists they are nested within. For example,
flatten([[]]) returns []
flatten([1]) returns [1]
flatten([[2,3]]) returns [2,3]
flatten([[1,[]],[[[2]],3]]) returns [1,2,3]
'''

def longest_chain(friends):
    for path_length in range(len(friends)):
        paths = all_combinations(list(friends.keys()), path_length)
        for path in paths:
            if verify_path(path, friends):
                return path_length
        
    return 0

def verify_path(path, friends):
    for i in range(len(path) - 1):
        if path[i+1] not in friends[i]:
            return False
    
    return True

def all_combinations(elems, n, start_list = []):
    if n == 0:
        return start_list
    
    all_combs = []

    for i in range(len(elems)):
        all_combs.extend(all_combinations(elems[:i] + elems[i + 1], n - 1, start_list + elems[i]))

    return all_combs