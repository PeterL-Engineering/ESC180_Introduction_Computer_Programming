#Deep Copies vs Shallow Copies

A = [[1, 2], [3, 4]]
B = A # B is an alias of A
      # B[anything] is just A[anything]

B = [A[0], A[1]] # same as A[:]
                 # B is not an alias of A
                 # B[0] is an alias of A[0]

B = A[:] # is a shallow copy
         # B is not an alias but its sublists are

# ===========

#Making a deep copy using for loop

A = [[1, 2], [3, 4], 5]
B = []
for sublist in A:
    B.append(sublist[:])

# Making a deep copy of a list of lists of lists

A = [[[0]], [[1]]]

B = []

for sublist in A:
    new_sublist = []
    for sublist_2 in sublist:
        new_sublist.append(sublist_2[:])
    B.append(sublist[:]) # Shallow copy of sublist [sublist[0]]

B[0][0][0] = 42 #Only changes the value in B