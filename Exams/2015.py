'''
2022 Q. 7 We can use a dictionary to record who is friends with whom by recording the lists of friends in a dictionary.
For example:
friends = {"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage"],
"Gottfried Leibniz": ["Carl Gauss"],
"Isaac Newton": ["Carl Gauss", "Charles Babbage"],
"Ada Lovelace": ["Charles Babbage", "Michael Faraday"],
"Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
"Michael Faraday": ["Ada Lovelace"] }
Here, Carl Gauss is friends with Isaac Newton, Gottfried Leibniz, and Charles Babbage. Assume that
friendships are symmetric, so that if X is friends with Y, then it’s guaranteed that Y is friends with X.
A friendship chain is a chain of people who are connected by friendship, with no repetitions allowed.
For example, the following is a friendship chain of length 5:
'''

def longest_chain(friends):
    for path_length in range(len(friends), -1, -1):
        paths = all_combinations(list(friends.keys()), path_length)
        for path in paths:
            if verify_friendship(path, friends):
                print(path)
                return path_length
    return 0

def all_combinations(elems, n, start_list = []):
    if n ==0:
        return start_list
    
    all_combs = []
    for i in range(elems):
        all_combs.extend(all_combinations(elems[:i]+elems[i+1:], n-1, start_list + elems[i]))
    return all_combs

def verify_friendship(path, friends):
    for i in range(len(path) - 1):
        if path[i+1] not in friends[i]:
            return False
    return True


'''
Q. 1 Write a function with the signature is_sorted(L) which takes in a list of ints L, and returns True iff the
list L is sorted, in either non-increasing or non-decreasing order. For example,
is_sorted([4, 5, 6, 1, 2, 3, 7]) should return False,
is_sorted([4, 5, 5, 6]) should return True,
is_sorted([6, 3]) should return True,
is_sorted([]) should return True.
'''

def is_sorted(L):
    if len(L) == 0 or len(L) == 1:
        return True
    
    L.sort()

    for i in range(len(L) -1):
        if L[i + 1] < L[i]:
            return False
    return True

'''
Q. 2 Write a function with the signature euc_distance(u, v) which computes the Euclidean distance between
the endpoints of the two sparse vectors u and v. Reminder: we store sparse vectors using dictionaries, with
only the non-zero entries being stored. For example, [4, 5, 0, 10, 0] is stored as {1:4, 2:5, 4:10}.
'''

def euc_distance(u, v):
    sum = 0
    
    for dimension in u.keys():
        if dimension not in v:
            sum += u[dimension]**2
        else:
            sum += (u[dimension] - v[dimension])**2
    
    for dimension in v.keys():
        if dimension not in u:
            sum += v[dimension]**2
    
    return sum**(1/2)

'''
Q. 3 Write a function with the signature movies_by_release_date(movies) which takes in a dictionary whose
keys are movie names and whose values are release dates, and which returns a list of movie names, in order
from the most recent release date to the earliest release date. The release dates are either in the format
"<year>, in <location>", or in the format "a long time ago, in <location>". Any movies released
"a long time ago" were released before the movies for which the year is indicated. Movies released at
the same time can be placed in the list in any order.
For example, if movies equals
{"Dude, Where’s My Death Star": "a long time ago, in a galaxy far far away",
"Star Wars: The Force Awakens": "2015, in Los Angeles",
"Star Wars": "1977, in Los Angeles",
"Sleepless in Aldera": "a long time ago, in Alderaan City",
"Jurassic World": "2015, in New York"},
movies_by_release_year(movies) can return
["Jurassic World", "Star Wars: The Force Awakens", "Star Wars",
"Sleepless in Aldera", "Dude, Where’s My Death Star" ].
'''

def movies_by_release_date(movies):

    sortable_movies = []

    for movie, release_date in movies.items():
        if "a long time ago" in release_date:
            sortable_movies.append((movie, -1))
        else:
            year = int(release_date.split(",")[0].strip())
            sortable_movies.append((movie, year))

    sorted_movies = sorted(sortable_movies.items(), key = lambda x: (-x[1]))

    return [movie[0] for movie in sorted_movies]

'''
Q. 4 Write a recursive function with the signature merge(L1, L2) which takes in two lists sorted in non-
decreasing order, and returns a list that contains all the elements from both L1 and L2, and is itself sorted.
You may not use loops, global variables, or helper functions, and the function signature must
be exactly as specified (i.e., you may not add additional parameters). You may not use Python’s
sorted() and sort() functions. You may use slicing.
For example, merge([4, 8, 10], [2, 5]) should return [2, 4, 5, 8, 10].
'''

def merge(L1, L2):

    if len(L1) == 0:        
        return L2
    elif len(L2) == 0:      
        return L1
    else:
        if L1[0] > L2[0]:           
            return [L2[0]] + merge(L1, L2[1:])
        else:           
            return [L1[0]] + merge(L1[1:], L2)
        