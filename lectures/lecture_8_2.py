#Question 5 From Midterm 2022

def haul_kid_house(hh, house, kid):
    '''Return the number of items kid kid collected 
    in house house'''
    if not kid in hh[house]:
        return 0
    else:
        return len(hh[house][kid])

def haul_kid(hh, kid):
    total = 0
    for house, house_dict in hh.items():
        total +=haul_kid_house(hh, house, kid)
    return total

def luckiest_kid(hh):
    '''Want to make a dictionary
    haul[kid] = haul for the kids 
    
    want a list of all the kids
    
    To get a list of all the kids, go through
    each house dict, extract the keys'''

    all_kids = []

    for house, house_dict in hh.items():
        for kid, haul in house_dict.items():
            all_kids.append(kid)

    haul = {}
    for kid in all_kids:
        haul[kid] = haul_kid(hh, kid)
    
    cur_luckiest_kid = "Roger"
    cur_max_items = -1
    for kid, num_items in haul.items():
        if cur_max_items < num_items:
            cur_max_items = num_items
            cur_luckiest_kid = kid
    return cur_luckiest_kid

#Mutability

'''
Lists and dictionaries are mutable, but tuples, ints and strs are not

Keys for dictionaries must be immutable
'''

#Sparse Matrices

'''
Values can be stored in a dictionary to limit the number of zeros eg.
'''

M = [[0, 5, 0], 
        [0, 0, 7]]

M_sparse = {(0, 1): 5, (1, 2): 7}

def zero_mat(dim):
    '''Return a matrix of size dim (dim is a tuple in the
    format (n rows, n cols) in a list of lists format,
    containing all zeros)'''

    # a list with n row elements
    #each elements is [0, ..., 0]

    res = []
    n_rows = dim[0]
    n_cols = dim[1]
    for i in range(n_rows):
        res.append([0] * n_cols)
    return res

def add_sparse_matrices(A, B, dim):
    z = zero_mat(dim)
    #A + B = 0 + A + B
    for coord, val in A.items():
        z[coord[0][1]] += val
    for coord, val in B.items():
        z[coord[0][1]] += val
    
    return z