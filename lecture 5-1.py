m = 15
n = 100
step = 17

for i in range (m, n, step):
    print(i)

i = m
while i < n:
    print(i)
    i += step

#

def praxify_str(s):
    return "In my opnion, " + s

res = "" #could say res = input("Enter an opinion: ")
stop_opinion = "praxis mt = <3"

while res != stop_opinion:
    res = input("Enter an opinion: ")
    print(praxify_str(res))

# input: n
# output: log10(n)

n = 1000
count = 0

while n > 1:
    n//= 10
    count += 1

#perfect square: a number where sqrt is an integer
#want to know how many perfect squares there are that are <= n

def is_perfect_square(k):
    '''Return true iff k is a perfect square'''
    for i in range(0, k+1):
        if i**2 == k:
            return True
    return False

def count_perfect_squares(n):
    '''Return the number of perfect squares <= n'''
    count = 0
    for  j in range(0, n+1):
        if is_perfect_square(j):
            count += 1
    return count