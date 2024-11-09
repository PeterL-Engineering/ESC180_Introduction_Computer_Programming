numbers = [1, 2, 6, 3, 7, 4, 8, 5, 9, 12]

# Attempt to remove numbers greater than 5

for num in numbers:
    if num > 5:
        numbers.remove(num)

print("Modified list:", numbers)

num_less_than_5 = []

for num in numbers:
    if num <= 5:
        num_less_than_5.append(num)

numbers = [1, 2, 6, 3, 7, 4, 8, 5, 9, 12]
# empty the list numbers
for num in numbers:
    numbers.remove(num)
print(numbers) # Doesn't work properly since the list is modified each iteration

# L.pop() returns and removes the last element o fL

L = [5, 6, 7]

L.pop() # return 7 and L = [5, 6]

L = ["brush teeth", "attend esc180"]

L1 = L

while len(L) > 0:
    L.pop()


L = []

L.append("PENDULUM")

'''
Things that change the variable
LHS = 

vs things that changes the contents
L[0] = 
L.pop()
'''