'''
Q. 1 In this question, your function will take in a list of integers L. Some of the integers may appear in the list
more than once. The function should return a list of all the integers that appear in the list L more than
once. The returned list should be sorted in increasing order, and must not contain duplicate integers: all
integers in the returned list must be unique.
'''
def get_repeating_ints(L):
    """Return a list of the integers that repeat in L, sorted in
    increasing order, with no duplicates."""

    temp = []
    repeating = []
    for i in range(len(L)):
        if L[i] not in temp:
            temp.append(L[i])
        else:
            repeating.append(L[i])
    
    return repeating

'''
Q. 2 Without using Python's sorted or list.sort functions, write a function that finds the median of a list
of an odd number of floats. The median of a list L of length n is a number such that at least (n - 1)/2
elements of L are smaller or equal to it, and at least (n - 1)/2 elements of L are larger or equal to it. For
example, my_median([5.0, 2.0, 4.0, 1.0, 3.0]) should return 3.0. There are no restrictions on the
runtime complexity of this function.
'''

def my_median(L):
    """Return the median of the list of floats L. Assume
    len(L) is odd.
    """
    n = len(L)

    for i in range(len(L)):

        smaller_or_equal = sum(1 for x in L if x <= L[i])

        larger_or_equal = sum(1 for x in L if x >= L[i])

        if smaller_or_equal >= (n-1)//2 and larger_or_equal >= (n-1)//2:
            return L[i]
        
'''
Q. 3 Santa received a list of gift requests, in the format of a Python list. An example list looks like
requests = ["socks", "calculus textbook", "calculator", "A+ in ESC180", "socks", ...]
Write a function that takes in a list like requests and returns the 10 most-requested items (i.e., the
top 10 items that appear the most often in the list). You can assume that there are no ties in the numbers
of times that items are requested. You can assume there are at least 10 different items in the list. The
return list should be alphabetically sorted.
'''
def top10requests(requests):
    requests_dict = {}

    for i in range(len(requests)):
        if requests[i] not in requests_dict:
            requests_dict[requests[i]] = 1
        else:
            requests_dict[requests[i]] += 1

    sorted_items = sorted(requests_dict.items(), key = lambda x: (-x[1], x[0]))

    top_10 = [i[0] for i in sorted_items[:10]]

    return top_10

'''
Q. 4 Write a function that takes in a list L, and returns a list that consists of every third element of L. For
example, every_third([5, 6, 7, 12, 0, 4, 6]) should return [7, 4]. You must use recursion.
You must not use global variables, for-loops, while-loops, or list comprehensions.
''' 
def every_third(L):

    if len(L) <= 2:
        return []
    else:
        return [L[2] + every_third[L[3:]]]
    
'''
Q. 5 Each of the subquestions in this question contains a piece of code. Treat each piece of code independently
(i.e., code in one question is not related to code in another), and write the expected output for each
piece of code. If the code produces an error, write down the output that the code prints before the error
is encountered, and then write “ERROR.” You do not have to specify what kind of error it is.
'''
#Part (a) [3 marks]
def f(L):
    L = ["holidays"]
L = ["happy"]
f(L) #Nothing happens
print(L) #['happy']

#Part (b) [3 marks]
L = [[[1, 2], 3], [4]]
L1 = [] 
for sublist in L:
    L1.append(sublist[:]) #[[[1, 2], 3], 4]
L[0][0][0] = 5 #[[[5, 2], 3], 4]
L[0][1] = 5 #[[[5, 2], 5], 4]
L[1][0] = 5 #[[[5, 2,] 5], 5]
print(L) #[[[5, 2,] 5], 5]
print(L1) #[[[5, 2], 3], 4]

#Part (c) [3 marks]
def doubler(L):
    dL = L
    for index in range(len(dL)):
        dL[index] = dL[index] * 2
L = [1, 2, 3]
doubler(L)
print(L) #[2, 4, 6]

#Part (d) [3 marks]
s1 = "HO HO HO"
s2 = s1
s1 = "Happy Holidays!"
print(s2)