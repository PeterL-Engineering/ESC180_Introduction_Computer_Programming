#Prime number check

def is_prime(n):
    if n == 2:
        return True
    
    for m in range, (2, n):
        # We want to check whether  is divisible by m
        #for m = 2, 3, 4, ... n-1
        if n % m == 0: # % not supported
            return False
        
    return True

# The following example needs import random

def inside_unit_circle(x, y):
    r_sq = x**2 + y**2
    return r_sq < 1

def estimate_pi(N):
    Am = 0
    for i in range(N):
        #x = random.random()
        #y = random.random()
        #if inside_unit_circle(x, y):
            Am += 1
    
    return 4*Am/N

# While loop example

i = 5
while i < 10:
    print (i) 
    i += 1

print("done")

if __name__== '__main__':
    is_prime(5)


        
