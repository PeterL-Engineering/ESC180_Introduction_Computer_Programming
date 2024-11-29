# Question 1

# a)

# The base case is x^0, recursive step is x * power (x, n-1)

# b)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
# c)

'''
power(2, 0)
                1
power(2, 1)
                1 * 2
power(2, 2)
                1 * 2 * 2
power(2, 3)
                1 * 2 * 2 * 2
'''

# Question 2

# Base is when the number is 0

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
       return n % 10 + sum_of_digits(n//10)
    
#print(sum_of_digits(100))

# Question 3
  
def remove_element(L, element):
    res = []
    temp = []

    for j in range (len(L)):
        if L[j] != element:
            temp.append(L[j])
        else:
            res.append(temp)
            temp = []

    if temp != []:
        res.append(temp)

    return res

print(remove_element([1, 2, 6, 4, 5, 3, 7], 3))

def remove_elements(L, elements):
    res = L
    temp = []
    for i in range(len(elements)):
        try:
            res[0][0]
            for list in res:
                temp.append(remove_element(list, elements[i]))
            
            res = temp
        except:
    
            res = remove_element(res, elements[i])
    return res

print(remove_elements([1, 2, 6, 4, 5, 3, 7], [3, 6]))
