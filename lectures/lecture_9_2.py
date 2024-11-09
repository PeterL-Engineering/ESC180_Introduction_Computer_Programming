n = 5
# for i in range(5)
# for i in range(n) it's the same

# for i in range(n)
# for i in list(range(n)) 

# same in terms of output but less 
# efficient because builds entire list

L = [1, 2, 3]
#for e in L:
#    L.append(2) # results in an infinite loop

L = [1, 2, 3, 4]
L.remove(2) #removes the first element of L 
            # that's equal to 2 -> L = [1, 3, 4]

L = [1, 2, 3, 4, 5]
for e in L:
    if e % 2 == 0:
        L.remove(e)

print(L)

L = [[1, 2], [3, 4]]
L1 = [L[0], L[1]]

# L and L1 are currently equal
# L and L1 are separate lists, not aliases
# BUT L[0] is an alias of L1[0] 
# and L[1] is an alias of L1[1]

# id(L[0]) == id(L1[0]) <- because those are aliases

L[0][0] = 5

# changing the contents of the alias of M
# changes the contents of M
# L[0] is an alias of L1[0]

# L[0][0] = smth <- changing the contents of L[0]

L1[0] = 4 # does not change L since we just change memory address 
          # of L1[0] to 1120 ie. address of 4 (see google doc)
