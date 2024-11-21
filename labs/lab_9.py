# Question 1

# Part a)

s = "OLD STRING"

def lowercase_string(string):
    return string.lower()

s = (lowercase_string(s))

# Part b)

L = [1, 2, 3]
print(id(L))

def g(List):
    List = List + [0, 0, 0]
    return List

L = g(L)
print(id(L))

def f(L):
    L[0] = 1

print(id(L))

# Part c)

d0 = {"A": 0, "B": 1}

print(id(d0))

def h(dictionary):
    dictionary = dictionary.copy()
    return dictionary

d0 = h(d0)
print(id(d0))

def k(dictionary):
    dictionary["A"] = 5

k(d0)
print(id(d0))

# Part d)

d1 = d0
d1["A"] = 2

print(d0)
print(d1)

# Part e)

import copy

def m(dictionary):
    dictionary = copy.deepcopy(d0)
    return dictionary

d1 = m(d1)
print(id(d1))

def p(dictionary):
    dictionary["A"] = 0

p(d1)
print(id(d1))

# Question 2

# Part a)

def binary_search(L, e):
    low = 0
    count = 0
    high = len(L)-1
    while high-low >= 2:
        count += 1
        mid = (low+high)//2 #e.g. 7//2 == 3
        if L[mid] > e:
            high = mid-1
        elif L[mid] < e:
            low = mid+1
        else:
            return (mid, count)
    if L[low] == e:
        return (low, count)
    elif L[high] == e:
        return (high, count)
    else:
        return None
    
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(List1, 8))
print(binary_search(List2, 9))

# Part b) (See above changes with count)

# Part c) You could construct a list where e is either 1/4 or 3/4 the way through

# Part d) 
import random

def list_maker(number_of_items):
    L = [None] * number_of_items
    for number in range(number_of_items):
        L[number] = random.randint(1, 100)

    L.sort()

    return L

list_of_10 = list_maker(10)
list_of_100 = list_maker(100)
list_of_million = list_maker(1000000)

print(binary_search(list_of_100, list_of_100[-1]))

# Part e)

import time
def calculate_runtime_binary(list):
    start = time.time()
    binary_search(list, list[-1])
    end = time.time()

    print(end-start)

calculate_runtime_binary(list_of_10)
calculate_runtime_binary(list_of_100)
calculate_runtime_binary(list_of_million)

def linear_search(L, e):
    for number in range(len(L)):
        if L[number] == e:
            return number
        
def calculate_runtime_linear(list):
    start = time.time()
    linear_search(list, list[-1])
    end = time.time()

    print(end-start)

calculate_runtime_linear(list_of_10)
calculate_runtime_linear(list_of_100)
calculate_runtime_linear(list_of_million)        