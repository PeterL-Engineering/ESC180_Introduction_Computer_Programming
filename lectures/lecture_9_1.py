#Debugging Infinite Loops

def counter(n):
    '''print 0 up to n'''

    i = 0

    #while i <= n:
    #    print(i)

# This is missing i += 1 after the print function

def counter_for(n):

    i = 0
    ii = 0

    for i in range(n+1):
        print(i)
        i += 1
        print(i)

    '''i = 0, i = 1, i = 1, ie. we double count'''

#Addresses of variables

x = "hi"

print(id(x))

y = "hi"

print(id(y)) #same id as x

L1 = [5, 6, 7]
L2 = L1
print(id(L1))
print(id(L2)) #same as L1

L1[0] = 7
print(L1, L2) #[7, 6, 7] [7, 6, 7]

for i in range(-10, 260):
    print (i, id(i))