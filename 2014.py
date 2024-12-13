'''
Q. 1 Write a function with the signature most_productive_elf(toys_produced) which takes in a dictionary
toys_produced whose keys are names of elves and whose values are the numbers of toys that each elf pro-
duced. The function should return the name of the elf who produced the most toys. For example, if toys0 is
{"Bob":4000, "Gloria":7000, "Hugo":6000, "Grumbles":42}, most_productive_elf(toys0) should
return "Gloria". Assume that no two elves produce equal numbers of toys.
'''

def most_productive_elf(toys_produced):

    sorted_list = sorted(toys_produced.items(), key = lambda x: (-x[1]))

    best_elf = sorted_list[0][0]

    return best_elf

'''
Q. 2 Write a function with the signature two_smallest(L) which takes in a list of ints L, and returns a list
with the two smallest elements of L, with the second-smallest element first and the smallest element second.
You can assume that all the elements of L are different from each other, and that L contains more than
one element. For example, two_smallest([5, 3, 10, 4]) should return [4, 3], since 3 and 4 are the
smallest elements of L, and 4 > 3. This function can have any runtime complexity you like.
'''

def two_smallest(L):
    second_small = float("inf")
    small = float("inf")

    for i in range(len(L)):
        if L[i] < small:
            second_small = small
            small = L[i]
        elif L[i] < second_small:
            second_small = L[i]
    
    return [second_small, small]

'''
Q. 3 M0 = [ [1, 2, 3, 4], [5, 0, 5, 0], [6, 7, 8, 9]]
Write a function with the signature largest_col_sum(M) which takes in a list of lists M which represents
a matrix in the format outlined above, and returns the sum of the column in the matrix whose sum is the
largest. For example, in the matrix M0 above, the third column has the largest sum: (3 + 5 + 8 = 16). So
largest_col_sum(M0) should return 16.
'''

def largest_col_sum(M):
    largest_sum = 0
    temp = 0

    for i in range(len(M[0])):
        for j in range(len(M)):
            temp += M[j][i]
        
        if temp > largest_sum:
                largest_sum = temp
        
        temp = 0
    
    return largest_sum

'''
Q. 6 Without using for- or while- loops, write a function with the signature filter_out_odds(L) which
takes in a list L of integers, and returns a new list that contains only the even integers in L, in the same
order as in L. For example, filter_out_odds([5, -2, 4, 0, 3, 7, 8]) should return [-2, 4, 0, 8].
Non-recursive solutions will earn at most 3 marks.
'''

def filter_out_odds(L):
    if len(L) == 0:
        return []
    elif L[0] % 2 == 0:
        return [L[0]] + filter_out_odds(L[1:])
    else:
        return filter_out_odds(L[1:])