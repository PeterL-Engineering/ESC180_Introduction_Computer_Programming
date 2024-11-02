def integer_square_root(n):
    '''Return sqrt(n)
    Assume that sqrt(n) is an integer'''
    for i in range(0, n+1):
        if i**2 == n:
            return 1
        return "ERROR"

def is_perfect_square(n):
    for i in range(0, n+1):
        if i**2 == n:
            return True
        return False

def is_perfect_square2(n):
    return integer_square_root(n) != "ERROR"

#def is_perfect_square3(n):
    #n**0.5
    #floor(25**0.5) = 5
    #floor(26**0.5) = 5
    #return math.floor(n**0.5)**2 == n
def n_perfect_sqaures(n):

    count = 0
    for j in range (0, n+1):
        if is_perfect_square(j):
            count +=1
        return count
    
def n_perfect_sqaures_fast(n):
    #keep computing next perfect square
    #count how many iterations it took to get
    # to a (perfect) square over n

    #count = 0
    cur_sq = -1
    i = -1
    while cur_sq <= n:
        i += 1
        cur_sq = i**2
        count += 1
    # return count - 1
    return i

#####

def property(n):
    return is_perfect_square(n) 
# You can just change the code of the the property function
# and simply leave the n_property function

def n_property(n):

    count = 0
    for j in range(0, n+1):
        if property(j):
            count += 1
    return count 
    
####
def artsie_math():
    operation = input("Operation: ")
    LHS_operand = float(input("LHS: "))
    RHS_operand = float(input("RHS: "))
    if operation == "+":
        return LHS_operand + RHS_operand
    elif operation == "-":
        return LHS_operand - RHS_operand
    else:
        print("ERROR: Artsies can't do complicated math")
