# If the player is at n, ar ethey guaranteed
# to win assuming they follow perfect strategy

# Player 1 is at 0 initially

# I know that if n is 18, player 1 loses
#                     19, player 1 wins
#                     20, player 1 wins
#                     21, player 1 wins

# Strategy:
# Write out bases cases
#       # Situations where we know the answer
# Express the answer to what the output of is
# in terms of calls to f itself

def is_win(n):
    if n == 21:
        return False
    if n == 20:
        return True
    if n == 19:
        return True
    
    moves = [1, 2]
    for move in moves:
        if not is_win(n+move):
            return True
    return False

#=================================

# Printing lists without loops

# Base case: empty list
#            print nothing

# Recursive step:
#            print L[0] and then print L[1:]

def print_list(L):
    '''Print the list L element-by element
    without using loops'''
    if len(L) == 0:
        return
    
    else:
        print(L[0])
        print_list(L[1:])

def print_list_reveerse(L):
    if len(L) == 0:
        return
    
    else:
        print(L[-1])
        print_list(L[:-1])