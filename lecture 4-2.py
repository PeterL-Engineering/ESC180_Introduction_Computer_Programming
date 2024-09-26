
def print_n_times(N, s):
    ''' print the string s N times'''
    for i in range (N):
        print(s)

def my_mult(A, B):
    my_sum = 0
    for i in range (B):
        my_sum += A
    return my_sum

def my_pow(A, B):
    res = 1
    for i in range(B):
        res *= A
    return res

def tell_n_times(message, N):
    for i in range(N):
        print("I'm telling you for the ", i, "-th time," , message)

def tell_n_times2(message, N):
    for i in range(N):
        if i == 1:
            print("I'm telling you for the ", i+1, "-st time," , message)
        elif i == 2:
            print("I'm telling you for the ", i+1, "-nd time," , message)
        else:
            print("I'm telling you for the ", i+1, "-th time," , message)

def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
if __name__=='main__':
    #print_n_times(1000, "authority")
 
    N = 100
    for i in range(N):
        print("RIGOUR")

    A = 3
    B = 5
    #0 + 3 + 3 + 3 + 3 + 3
    my_sum = 0
    #add 3 into my_sum 5 times
    for i in range(5):
        my_sum += 3
    #my sum will be 15 after the loop ended

    my_sum = 0
    for i in range(B):
        my_sum += A

    print(my_pow(3, 1))

    for i in range(100):
        print("The value of 1", 1)

    tell_n_times("Start Project 1", 15)

    