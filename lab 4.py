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

#Question 3

def gcd(n, m):
    divisor = 1
    if n > m:
        for j in range(1, n+1):
            if n % j == 0 and m % j == 0:
                divisor = j
    else:
        for j in range (1, m+1):
            if n % j == 0 and m % j == 0:
                divisor = j
    return divisor

if __name__ == '__main__':
    gcd(3,6)