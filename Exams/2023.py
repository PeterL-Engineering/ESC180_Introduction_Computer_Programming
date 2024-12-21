'''
Q. 1 Santa has a list of names and the corresponding list of gifts he plans to give to each child. Write a function
that uses a loop to print out a message for each child, telling them what gift they will receive. For example,
if the names are stored in the list names = ["Alice", "Bob", "Charlie"] and the gifts are stored in the
list gifts = ["robot", "train", "EngSci admission offer"], the function should print:
Alice will receive: robot
Bob will receive: train
Charlie will receive: EngSci admission offer
You can assume that the input is valid, i.e., that the length of names is the same as the length of gifts.
The function should print something rather than return anything
'''

def print_gifts(names, gifts):
    for i in range(len(names)):
        print(names[i] + "will receive: " + gifts[i])

'''
Q. 2 Given a matrix M stored as a list of lists, i.e. the matrix

is stored as [[1,2,3], [4,5,6]], write a function is_entry_in_matrix(e, M). The function returns
True if at least one of the entries in M is equal to e, and False otherwise. Sample usage:
is_entry_in_matrix(3, [[1,2,3], [4,5,6]]) # True
is_entry_in_matrix(9, [[1,2,3], [4,5,6]]) # False
is_entry_in_matrix(1, [[1,2,3], [4,1,6]]) # True
'''

def is_entry_in_matrix(e, M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == e:
                return True
    return False

'''
Q. 3 You are given a list L consisting of a combination of the elements "w", "b", "". Write a function
has_three_white_in_a_row(L). The function returns True if the list L contains at least one sequence
of 3 consecutive "w"s that is not a part of a sequence of 4 or more consecutive "w"s, and returns False
otherwise. Sample usage:
has_three_white_in_a_row(["", "b", "w", "w", "w", "b"]) # True
has_three_white_in_a_row(["b", "w", "w", "", "w", "b"]) # False
has_three_white_in_a_row(["", "w", "w", "w", "w", "b"]) # False
has_three_white_in_a_row(["w", "w", "w", "", "w", "w", "w"]) # True
has_three_white_in_a_row(["w", "w", "w", "w", "w", "w"]) # False
'''

def has_three_white_in_a_row(L):
    count = 0

    for i in range(len(L)):
        if L[i] != "w":
            count = 0
            continue
        else:
            if count == 3:
                return True
            
            count += 1
    
    return False
        
'''
Q. 4 Write a function merge_dict(A, B) that takes in two dictionaries A and B, and returns a new dictionary
that contains the “merged” dictionary consisting of all the information in A and B. The merged dictionary
should have all the keys in both A and B, with the corresponding values. If a key in A is the same as a key
in B, collect the values in a list as the value for that key in the merged dictionary. Sample usage:
dict1 = {10: "exams", 20: "holidays", "winter": "break"}
dict2 = {30: "lights", "winter": "snow"}
merge_dict(dict1, dict2)
# {10: "exams", 20: "holidays", 30: "lights", "winter": ["break", "snow"]}
'''

def merge_dict(A, B):
    merged = {}

    for key, value in B.items():
        merged[key] = value

    for key, value in A.items():
        if key in merged:
            merged[key] = [merged[key]]
            merged[key].append(value)

        else:
            merged[key] = value

    return merged

'''
Q. 5 You are given a string sentence. Assume sentence has no punctuation marks, all the words in the
sentence are separated by a single white space, and all words in sentence consist of only lower-case
letters.
Write a function remove_duplicate_words(sentence) that returns a string with all the duplicate words
of the sentence removed. Keep the first instance for each duplicated word. Sample usage:
sentence = "happy holidays hope santa gives you a nice gift for the holidays that makes you happy"
remove_duplicate_words(sentence)
# "happy holidays hope santa gives you a nice gift for the that makes you"
'''

def remove_duplicate_words(sentence):
    res = []

    for word in sentence.split():
        if word in res:
            continue
        else:
            res.append(word)
        
    return " ".join(res)

'''
Q. 6 Write a function log(b,n) that returns the base b logarithm of n. Both b and n are floats that are greater than
1.0. Round the result down to the nearest integer. You must not import any modules, including math.
'''

def log(b, n):
    res = 0

    while n >= b:
        n = n / b
        res += 1

    return int(res)

# Runtime Complexity is O(logb(n))

'''
Q. 7
'''
def longest_chain(friends):
    for path_length in range(len(friends)):
        paths = all_combinations(list(friends.keys()), path_length)
        for path in paths:
            if verify_friends(path, friends):
                return path_length
    return 0

def all_combinations(elems, n, start_list = []):
    if n == 0:
        return start_list
    
    all_combs = []
    for i in range(len(elems)):
        all_combs.extend(all_combinations(elems[:i] + elems[i+1:], n-1, start_list + elems[i]))

def verify_friends(path, friends):
    for i in range(len(path) - 1):
        if path[i + 1] not in friends[i]:
            return False
    return True

'''
Q. 8 Write a function that takes in a list L of positive integers, and returns a list that consists of every second element of
L, except that it skips every second even number encountered. You must use recursion. You must not use for-loops,
while-loops, or list comprehensions (N.B.: if you don’t know what list comprehensions are, don’t worry about it: we
haven’t covered them, and it is not possible to use them accidentally).
For example, if the input is
[1, 2, 3, 0, 10, 11, 12, 16, 20], the function would return
[1, 2, 3, ,10, 11, ,16]
Above, the list are displayed in to ease understanding: the spaces don’t matter. Note that the 0, the 12, and the
20 are skipped because they are the 2-nd, the 4-th, and the 6-th even numbers in the list
'''

def list_sorter(L, even_count = 0, second_count = 1):
    if len(L) == 0:
        return []
    
    if second_count % 3 == 0:
        if even_count % 2 == 0:
            if L[0] % 2 == 0:
                return list_sorter(L[1:], even_count + 1, second_count + 1)
            else:
                return [L[0]] + list_sorter(L[1:], even_count, second_count + 1)
        else:
            if L[0] % 2 == 0:
                return [L[0]] + list_sorter(L[1:], even_count + 1, second_count + 1)
            else:
                return [L[0]] + list_sorter(L[1:], even_count, second_count + 1)
    else:
        if L[0] % 2 == 0:
            return list_sorter(L[1:], even_count + 1, second_count + 1)
        else:
            return [L[0]] + list_sorter(L[1:], even_count, second_count + 1)