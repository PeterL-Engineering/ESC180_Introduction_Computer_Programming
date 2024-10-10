#Question 1

def lebniz_formula_for(n):
    res = 0
    for i in range(n+1):
        res += ((-1)**i / (2 * i )) + 1
    return res

#Question 2

def lebniz_formula_while(n):
    res = 0
    count = 0
    while count < n:  # Use n for iterations
        res += ((-1)**count / (2 * count)) + 1  # Update to use count
        count += 1
    return res  # Return the result

#Question 3a

def gcd1(n, m):
    divisor = 1
    if n == 0 or m == 0:
        return max (n, m)
    if n > m:
        for j in range(1, n+1):
            if n % j == 0 and m % j == 0:
                divisor = j
    else:
        for j in range (1, m+1):
            if n % j == 0 and m % j == 0:
                divisor = j
    return divisor

#Question 3b

def gcd2(n, m):
    if n == 0 or m == 0:
        return max(n, m)  # Handle cases where one number is zero
    
    divisor = min(n, m)  # Start from the smaller number
    
    while divisor > 0:  # Loop until we find a common divisor
        if n % divisor == 0 and m % divisor == 0:
            return divisor
        divisor -= 1
    
    return 1  # If no common divisor found, return 1

#Question 4

def simplify_fractions(n, m):

    gcd = gcd2(n, m)

    simplified_n = n / gcd
    simplified_m = m / gcd

    return (simplified_n/simplified_m)

#Question 5

def enter_names():
    names = []  # Initialize an empty list to store names
    while True:
        name = input("Enter a name: ")  
        if name == "END":  # Check for the exit condition
            break
        names.append(name)  # Add the name to the list
    
    return ', '.join(names) 

#Question 6
import math

def calculate_pi(n):
    pi = (round(math.pi*(10**n)))

    count = 0
    estimate = 0

    while round(4 *(estimate) * (10**n)) != pi:
        estimate += ((-1)**count) / ((2 * count) + 1) 
        count += 1

    return count

#Question 7

if __name__ == '__main__':
    #print(round(math.pi*(10**5)))
    print(calculate_pi(2))
    print(gcd1(1, 2))
    print(gcd2())