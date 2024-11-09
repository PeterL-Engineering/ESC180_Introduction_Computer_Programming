import numpy as np


# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
print(M)

#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)        

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist() 

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

#Part A

def pass_or_fail(course):
    while course == "Calculus":
        continue
    #return pass error

def pass_or_fail(course):
    if course != "Calculus":
        return "pass"

#Part B

# Question 1

def print_matrix(M_lol):
    print("[")
    for i in range(len(M_lol)):
        for j in range(len(M_lol[0])):
            print(M_lol[i][j])
            if j == len(M_lol[0] - 1):
                print("] \n")

# Question 2

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return row[i]
        else:
            return len(row)
        
# Question 3

def get_row_to_swap(M, start_i):
    row_to_swap = start_i
    col_of_non_zero = len(M[0])
    for i in range(start_i, len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 0 and j < col_of_non_zero:
                col_of_non_zero = j
                row_to_swap = i
    
    if row_to_swap != start_i:
        M[row_to_swap],M[start_i] = M[start_i], M[row_to_swap]

    return M

# Question 4

def add_rows_coefs(r1, c1, r2, c2):

    new_list = [0] * len(r1)

    for i in range(len(new_list)):
        new_list[i] = r1[i] * c1 + r2[i] * c2

    return new_list

# Question 5

def eliminate(M, row_to_sub, best_lead_ind):
    for row in range(row_to_sub + 1, len(M)):
        if M[row][best_lead_ind] == 0:
            continue

        addition_coeff = -M[row][best_lead_ind] / M[row_to_sub][best_lead_ind]

        for column in range(len(M[0])):
            M[row][column] += M[row_to_sub][column] * addition_coeff

    return M
            
# Question 6

def forward_step(M):
    num_cols = len(M[0])
    num_rows = len(M)
    
    for row in range(1, num_rows):
        for lead in range(num_cols):
            
            M = get_row_to_swap(M, row)

            print("Swapped row", str(row))

            if M[row][lead] == 0:
                continue

            M = eliminate(M, row, lead)

            print("Eliminated row", str(row))
            break

    return M

# Question 7

def backward_step(M):
    num_rows = len(M)
    num_cols = len(M[0])

    for i in range(num_rows - 1, 0, -1):
        for j in range(i, 0, -1):
            for k in range(len(M[0])):
                M[j][k] = 
        

        




